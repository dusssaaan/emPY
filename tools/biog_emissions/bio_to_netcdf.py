#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:02:56 2020

@author: p6001
"""
import datetime
import numpy as np
import netCDF4
import os

#writing to netcdf ############################################################################
def biog_to_netCDF(output_dir,out_file_name,dic_biog,projection,grid_params):
        
       
    if not os.path.exists(output_dir):
       os.makedirs(output_dir)

    
    global_params={ 'CDATE':np.int32('{0}{1:03d}'.format(datetime.datetime.today().year,datetime.datetime.today().timetuple().tm_yday)),
                    'P_ALP':projection['lat_1'],
                    'P_BET':projection['lat_2'],
                    'P_GAM':projection['lon_0'],
                    'XCENT':projection['lon_0'],
                    'YCENT':projection['lat_0'],
                    'CTIME':np.int32(63057),
                    'DATE_TIME':np.int32(2),
                    'EXEC_ID':"???????????????? ",
                    'FILEDESC':"b3grd file",
                    'FTYPE':np.int32(1),
                    'GDTYP':np.int32(2),
                    'HISTORY':"",
                    'IOAPI_VERSION':"Id",
                    'NC_STEP':np.int32(1),
                    'NLAYS':np.int32(1),
                    'NTHIK':np.int32(1),
                    'NVARS':np.int32(len(dic_biog.keys())),
                    'SDATE':np.int32('{0}{1:03d}'.format(datetime.datetime.today().year,datetime.datetime.today().timetuple().tm_yday)),
                    'STIME':np.int32(0),
                    'TSTEP':np.int32(0),
                    'UPNAM':"OPENEOUT        ",
                    'VAR-LIST':"".join('{0:16s}'.format(f) for f in dic_biog.keys()),
                    'VGLVLS':np.array([0., 0],dtype='float32'),
                    'VGTOP':np.float32(0.),
                    'VGTYP':-np.int32(1),
                    'WDATE':np.int32('{0}{1:03d}'.format(datetime.datetime.today().year,datetime.datetime.today().timetuple().tm_yday)),
                    'WTIME':np.int32(63057),
                    'NCOLS':np.int32(grid_params['nj']),
                    'NROWS':np.int32(grid_params['ni']),
                    'XORIG':grid_params['XORIG'],
                    'YORIG':grid_params['YORIG'],
                    'XCELL':grid_params['XCELL'],
                    'YCELL':grid_params['XCELL'],
                    'GDNAM':f"{out_file_name}"}
   
    
    with netCDF4.Dataset('{0}/{1}.nc'.format(output_dir,out_file_name),mode='w') as out:
    
         # create globals
         for global_par in global_params:
                         
            out.setncattr(global_par, global_params[global_par])

         # create dimensions
        
         out.createDimension('TSTEP', None)
         out.createDimension('DATE-TIME', size=global_params['DATE_TIME'])
         out.createDimension('LAY', size=global_params['NLAYS'])
         out.createDimension('VAR', size=global_params['NVARS'])
         out.createDimension('COL', size=global_params['NCOLS'])
         out.createDimension('ROW', size=global_params['NROWS'])
         
         # create TFLAGS
         out.createVariable('TFLAG', np.int32, ('TSTEP', 'VAR', 'DATE-TIME'),fill_value=None)
         out.variables['TFLAG'].setncatts({'units': "<YYYYDDD,HHMMSS>", 'long_name': "TFLAG", 'var_desc': "Timestep-valid flags:  (1) YYYYDDD or (2) HHMMSS"})     
         
         
         tflag=np.zeros([1,global_params['NVARS']],dtype=int)

         out.variables['TFLAG'][:,:,1]=tflag
         out.variables['TFLAG'][:,:,0]=0#2017001
         #np.int32('{0}{1:03d}'.format(datetime.datetime.today().year,datetime.datetime.today().timetuple().tm_yday))
         
         
         # create variables
         for name in dic_biog:
             
             out.createVariable(name, np.float32, ('TSTEP', 'LAY', 'ROW', 'COL'),fill_value=None)
             
             if (not name.startswith('AVG_NO')  and  not name.startswith('LAI') ):
                 out.variables[name].setncatts({'units': 'gramsC/hour', 'long_name': name, 'var_desc':'normalized emissions' })     
             elif name.startswith('LAI'): 
                 out.variables[name].setncatts({'units': 'index', 'long_name': name, 'var_desc':'normalized emissions' })
             else:
                 out.variables[name].setncatts({'units': 'gramsN/hour', 'long_name': name, 'var_desc':f'normalized emissions for NO {name[6:]} ' })

                
             out.variables[name][:,:,:,:]=dic_biog[name] 
             
             
             
             
             
             
             
             
             
             
             
             
