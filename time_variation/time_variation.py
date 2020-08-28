#!/usr/bin/env /data/juraj/anaconda3/envs/geo/bin/python
"""
TIME VARIATION SCRIPT

Function:    
reading numpy arrays after speciation, preparing time matrices from time maping and time series files,
applying the time matrices to the numpy arrays,
saving the emissions to netcdf files

now you need read old netcdf file in which the fields will be saving 

Libraries and moduls needed:
libraries: pandas, numpy, netCDF4, time, pytz, datetime, os, netCDF4

Revision History:
    
28.01.2019 D. Stefanik: creating first version of script

"""
# import proper libraries
import pandas as pd
import time
import os
import datetime
import netCDF4
import time_matrix as tm
import grided_emision_time as gt
import point_emision_time as pt
import sys
sys.path.append('/data/dusan/EMPYS/case_run')
from config_file import grid_params, projection
import numpy as np

# parameters of grid
ni = grid_params['ni']
nj = grid_params['nj']
nlays = grid_params ['nlays']


#species_write to netcdf file
cmaq_sp=['PAR','PNO3','IOLE','BAP','PSO4','PEC','CO','POC','SO2','OLE','ISOP','TERP',
         'NO2','ALDX','CH4','XYL','NH3','ETOH','ETHA','FORM','TOL','PMC','ETH','PMFINE','ALD2','BENZENE','NO','NR','MEOH']


#start datum
datum_start=datetime.datetime(2017,1,1,0)
#end day
datum_end=datetime.datetime(2017,1,1,0)


#path for input speciated files
input_dir='/data/em/data/outputs-speciation-d03-2017_WB/'

#output path
output_dir='/data/dusan/EMPYS/data/outputs-final-skusanie'
#name of output files in form out_file_name-datum
out_file_name='EM_SKUSANIE'


#define main time ZONE of domain names must be recognized by library pytz
T_ZONE='Europe/Prague'



###############seting the time variation static data 
#tv_mapping
tv_mapping=pd.read_csv('/data/em/time_variation/static_data/tv_map_em.csv')
tv_values=pd.read_csv('/data/em/time_variation/static_data/tv_values.csv') 
#tv_series
tv_series=pd.read_csv('/data/em/time_variation/static_data/tv_series.csv')
#emission category file in order to know how to mapping parent categories
em_cat_file=pd.read_csv('/data/dusan/EMPYS/speciate/emission_categories_sp.csv')


#proper netcdf
emis=netCDF4.Dataset('/data/oko/emisie_2017/WB_2017_d01-2017-01-01.nc')



#########################################################################################################
# proper sript, nothing to set up
#########################################################################################################
start_time = time.time()


if not os.path.exists(output_dir):
   os.makedirs(output_dir)

###### Looping for the days ##############################################################
datum=datum_start

dic_time_map=dict(zip(em_cat_file['cat_id'], em_cat_file['time_profile']))
while datum <= datum_end :
    
    dim=25
    dic_time_matrix=tm.time_matrix(T_ZONE, tv_values, tv_mapping, tv_series, em_cat_file, datum, dim)
    
    dic_species=gt.numpy_time_variation_matrix(input_dir,cmaq_sp,dic_time_matrix, dic_time_map,dim,nlays,ni,nj)
   
    gt.gridded_to_netCDF_OLD(output_dir,out_file_name,dic_species,datum,projection,grid_params)
    
    datum += datetime.timedelta(days=1)
    
print('Program run succesfully:-) in {0:.1f} sec'.format(time.time() - start_time)) 


points=pd.read_csv('/data/dusan/EMPYS/data/outputs-speciation-skusanie/point_sources/speciate_points')


points=pt.point_data_frame('/data/dusan/EMPYS/data/outputs-speciation-skusanie/point_sources/speciate_points',cmaq_sp)

list_time_categories_used=pt.time_profiles(dic_time_map,em_cat_file,points)

arrays=pt.arrays(list_time_categories_used,em_cat_file,points,dim,dic_time_matrix,cmaq_sp)

pt.point_to_netCDF(output_dir,'EM_SKUSANIE_STACK',arrays,datum,projection,grid_params)

print('Program run succesfully:-) in {0:.1f} sec'.format(time.time() - start_time)) 

    
    



    
    
    
""""
#preparing mapping from category to the time_variation category###############################################################################
#######prepare new emission category file
dic_parent_list={}
for index, row in em_cat_file.iterrows():
    category=row['cat_id']
    parent=row['parent']
    dic_parent_list[category]=[]
    
    while parent !=0: 
          
          dic_parent_list[category].append(parent)
          
          parent=int(em_cat_file[em_cat_file['cat_id']==parent]['parent'])


mapping_categories=list(set(tv_mapping['snap'].unique()) | set(tv_series['cat_id'].unique()))

em_cat_file=pd.read_csv('/data/dusan/EMPYS/speciate/emission_categories_sp.csv')



#############################
em_cat_file=pd.read_csv('/data/dusan/EMPYS/speciate/emission_categories_sp.csv')
em_cat_file=em_cat_file[~em_cat_file['cat_id'].isin([10000001,10000002,10000003,11000000])]


em_cat_file['time_profile']=0
for index, row in em_cat_file.iterrows():
    if row['cat_id'] in mapping_categories:
       print(row['cat_id'])
       em_cat_file.loc[index,['time_profile']]=row['cat_id']
    else:
       
       param=False
       n=0
       while param==False:
             parent=dic_parent_list[row['cat_id']][n]
             if parent in mapping_categories:
                param=True 
             else:
                n+=1 
       em_cat_file.loc[index,['time_profile']] = parent          
       print('!!!!!!!!!!!!!! not in spec',row['cat_id'],'for spec use', parent,'n',n) 
#######################################################################################################
em_cat_file.to_csv('/data/dusan/EMPYS/speciate/emission_categories_sp.csv',index=False)
"""
    
    
    
    
    
    
    