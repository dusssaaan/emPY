#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:57:49 2020

@author: p6001
"""
import netCDF4
import numpy as np
import pandas  as pd


def biog(bfac_path,beld4_path):

    
    bfac=pd.read_csv(bfac_path, names=['beld4_name','type','units','factor'])
    beld4=netCDF4.Dataset(beld4_path)
    
    
    #declaration of agricultural files 
    ag=['NLCD_81', 'NLCD_82', 'MODIS_12', 'MODIS_47', 'Alfalfa', 'Alfalfa_ir', 'Barley', 'Barley_ir', 'CornGrain',
        'CornGrain_ir', 'CornSilage', 'CornSilage_ir', 'Cotton', 'Cotton_ir', 'Other_Grass', 'Other_Grass_ir', 'Hay',
        'Hay_ir', 'Other_crop', 'Other_crop_ir', 'Oats', 'Oats_ir', 'Peanuts', 'Peanuts_ir', 'Potatotes', 'Potatotes_ir',
        'Rice', 'Rice_ir', 'Rye', 'Rye_ir', 'SorghumGrain', 'SorghumGrain_ir', 'SorghumSilage', 'SorghumSilage_ir',
        'Soybeans', 'Soybeans_ir', 'Beans', 'Beans_ir', 'BeansEdible', 'BeansEdible_ir', 'Canola', 'Canola_ir',
        'Wheat_Spring', 'Wheat_Spring_ir', 'Wheat_Winter', 'Wheat_Winter_ir']
    
    #declaration of pollutant names 
    B3V14DIMS3_names=['ISOP', 'MBO', 'METH','APIN', 'BPIN', 'D3CAR','DLIM', 'CAMPH', 'MYRC', 'ATERP', 'BPHE',
    'SABI', 'PCYM' , 'OCIM', 'ATHU', 'TRPO','GTERP', 'ETHE', 'PROPE', 'ETHO', 'ACET', 'HEXA', 'HEXE', 'HEXY', 'FORM',
    'ACTAL', 'BUTE', 'ETHA', 'FORAC','ACTAC', 'BUTO', 'CO', 'ORVOC', 'NO','SESQT']
    
    #NO names
    NO_names=['AVG_NOAG_GROW', 'AVG_NOAG_NONGROW', 'AVG_NONONAG']
    
    bfac['beld4_name|type']=bfac.apply(lambda x : f"{x['beld4_name']}|{x['type']}",axis=1 )
    dic_emfac=dict(zip(bfac['beld4_name|type'],bfac['factor']))
    def emfac(beld4_name,name): return dic_emfac[beld4_name+ '|' +name ]
    
    ############################
    dic_biog={}
    for name in B3V14DIMS3_names:
        
        if name !='NO':
           dic_biog[f'AVG_{name}S'] =0 
           dic_biog[f'AVG_{name}W'] =0
        if name in ['ISOP','MBO','METH']:
           dic_biog[f'LAI_{name}S'] =0  
           dic_biog[f'LAI_{name}W'] =0
           dic_biog[f'AVG_{name}S'] =0
           
    dic_biog.update({key: 0 for key in NO_names})
    #############################
    
    
    fac_km2=144/100
    
    for land_use in beld4.variables.keys():
        if land_use  == 'TFLAG': pass
           
        elif land_use not in bfac['beld4_name'].unique():
              print('#####################')
              print(f'!!!! Warning land use {land_use} not defined in b360fac file') 
              print('#####################')    
        else:   
            
           land_use_km2=np.array(beld4.variables[land_use])*fac_km2 
           
           for  name in B3V14DIMS3_names:
                
                if name == 'NO': # and np.sum(land_use_km2) > 0:
            
                    if land_use in ag:
                             
                           dic_biog['AVG_NOAG_NONGROW']+= land_use_km2*emfac(land_use,name) 
                           
                           if  land_use == 'MODIS_14':
                               
                                 dic_biog['AVG_NOAG_GROW'] += land_use_km2*emfac(land_use,name)*0.333333 
                                 
                                 dic_biog['AVG_NONONAG'] += land_use_km2*emfac(land_use,name)*0.333333
                           
                           else: 
                                 dic_biog['AVG_NOAG_GROW'] += land_use_km2*emfac(land_use,name)                     
                                           
                    else:        
                           dic_biog['AVG_NONONAG'] += land_use_km2*emfac(land_use,name)
                        
                if name != 'NO': #and np.sum(land_use_km2) > 0:
                   
                    dic_biog[f'AVG_{name}S'] +=land_use_km2*emfac(land_use,name)
                    
                    dic_biog[f'AVG_{name}W'] +=land_use_km2*emfac(land_use,name)*emfac(land_use,'WFAC')
                
                    if name in ['ISOP','MBO','METH']:
                       
                       dic_biog[f'LAI_{name}S'] += land_use_km2*emfac(land_use,name)*emfac(land_use,'LAI')
                        
                       dic_biog[f'LAI_{name}W'] += land_use_km2*emfac(land_use,name)*emfac(land_use,'LAI')*emfac(land_use,'WFAC')
                    
    
    for name in ['ISOP','MBO','METH']:
        dic_biog[f'LAI_{name}S']=np.divide(dic_biog[f'LAI_{name}S'], dic_biog[f'AVG_{name}S'], out=np.zeros_like(dic_biog[f'LAI_{name}S']), where=dic_biog[f'AVG_{name}S']!=0)
        dic_biog[f'LAI_{name}W']=np.divide(dic_biog[f'LAI_{name}W'], dic_biog[f'AVG_{name}W'], out=np.zeros_like(dic_biog[f'LAI_{name}W']), where=dic_biog[f'AVG_{name}W']!=0)

    return dic_biog;

        