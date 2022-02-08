#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 08:29:06 2020

@author: p6001
"""
case_path='../../case_run'

import numpy as np
import netCDF4
import importlib
import sys

import normbeis3
importlib.reload(normbeis3)
import bio_to_netcdf
sys.path.append(case_path)
import emPY_config_file
importlib.reload(emPY_config_file)

projection=emPY_config_file.projection
grid_params=emPY_config_file.grid_params
out_file_name='B3GRD_D02_new'
output_dir='/data/oko/dusan/emisie'

####################################################################################################
# prepare b360fac file
bfac_path='/data/oko/dusan/emisie/b360fac_beld4_csv_nlcd2006.txt'

'''
# prepare dic with land use in km2
beld4_netcdf=netCDF4.Dataset('/data/oko/dusan/emisie/beld4_12kmCONUS_2011nlcd_bench.nc')
# if you need to convert in km2
fac_km2=144/100

beld4={}
for _ in beld4_netcdf.variables:
    if _ != 'TFLAG':
       beld4[_] = np.array( beld4_netcdf.variables[_][:] )*fac_km2
'''  
"""
vlado=np.array(netCDF4.Dataset('/data/oko/dusan/emisie/USGS_mala.nc').variables['variable'][:])
vlado[vlado<0 ] = 0
a=[ 'MODIS_0', 'MODIS_1', 'MODIS_2', 'MODIS_3', 'MODIS_4', 'MODIS_5',
       'MODIS_6', 'MODIS_7', 'MODIS_8', 'MODIS_9', 'MODIS_10', 'MODIS_11',
       'MODIS_12', 'MODIS_13', 'MODIS_14', 'MODIS_15', 'MODIS_16',
       'MODIS_17', 'MODIS_254', 'MODIS_255']

beld4={}
for _ in a: beld4[_]=np.zeros([1,1,103, 184])

fac_km2=4.710621094*4.710621094/100

beld4['MODIS_0'][0,0,:]=vlado[14,:]*fac_km2
beld4['MODIS_1'][0,0,:]=vlado[3,:]*fac_km2
#beld4['MODIS_2'][0,0,:]=vlado[,:]*fac_km2
#beld4['MODIS_3'][0,0,:]=vlado[,:]*fac_km2
beld4['MODIS_4'][0,0,:]=vlado[9,:]*fac_km2
beld4['MODIS_5'][0,0,:]=vlado[11,:]*fac_km2
#beld4['MODIS_6'][0,0,:]=vlado[,:]*fac_km2
beld4['MODIS_7'][0,0,:]=vlado[6,:]*fac_km2
#beld4['MODIS_8'][0,0,:]=vlado[,:]*fac_km2
#beld4['MODIS_9'][0,0,:]=vlado[,:]*fac_km2
beld4['MODIS_10'][0,0,:]=vlado[5,:]*fac_km2
#beld4['MODIS_11'][0,0,:]=vlado[,:]*fac_km2
beld4['MODIS_12'][0,0,:]=vlado[1,:]*fac_km2
beld4['MODIS_13'][0,0,:]=vlado[0,:]*fac_km2
#beld4['MODIS_14'][0,0,:]=vlado[,:]*fac_km2
beld4['MODIS_15'][0,0,:]=vlado[15,:]*fac_km2
#beld4['MODIS_16'][0,0,:]=vlado[,:]*fac_km2
#beld4['MODIS_17'][0,0,:]=vlado[,:]*fac_km2
#beld4['MODIS_254'][0,0,:]=vlado[,:]*fac_km2
#beld4['MODIS_255'][0,0,:]=vlado[,:]*fac_km2
"""
a=[ 'MODIS_0', 'MODIS_1', 'MODIS_2', 'MODIS_3', 'MODIS_4', 'MODIS_5',
       'MODIS_6', 'MODIS_7', 'MODIS_8', 'MODIS_9', 'MODIS_10', 'MODIS_11',
       'MODIS_12', 'MODIS_13', 'MODIS_14', 'MODIS_15', 'MODIS_16',
       'MODIS_17', 'MODIS_254', 'MODIS_255']

beld4={}
for _ in a: beld4[_]=np.zeros([1,1,103, 184])

fac_km2=4.710621094*4.710621094/100

import rioxarray
import os


for i in os.listdir('/data/oko/dusan/emisie/vlado_modis'):
    vrstva = rioxarray.open_rasterio('/data/oko/dusan/emisie/vlado_modis/'+i).data[:]
    beld4['MODIS_'+i[10:]][0,:]=vrstva
    
######################################################################################################

dic_biog=normbeis3.biog(bfac_path,beld4)    


bio_to_netcdf.biog_to_netCDF(output_dir,out_file_name,dic_biog,projection,grid_params)


for key in dic_biog:
    print(key)
    print(np.sum(dic_biog[key]))


