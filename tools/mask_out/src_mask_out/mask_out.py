"""
MASK SCRIPT

Function:    
creating 2D numpy array with zero for the grid cell if the cell falls 
in the shapefile and 1 if the grid cell do not falls in the shapefile
if the cell falls in the shapefile partialy the value between (0,1) is 
assign to the grid cell according the area of intersect

Libraries and modules needed:
libraries: geopandas, numpy, shapely, time, os
modules:

Revision History:
    
30.01.2019 D. Stefanik: creating first version of script
"""


import geopandas as gpd
import numpy as np
import shapely
import time
import os



def create_mask(shape_file_dir, output_dir, name, projection, grid_params):

    if not os.path.exists(output_dir):
       os.makedirs(output_dir)
    
    shape_file=gpd.read_file(shape_file_dir)
    
    
    XORIG=grid_params['XORIG']
    YORIG=grid_params['YORIG']
    XCELL=grid_params['XCELL']
    nj=grid_params['nj']
    ni=grid_params['ni']
    
    
    start_time = time.time()
    
    
    shape_file=shape_file.to_crs(projection)
    
    geometry_of_mask=shape_file['geometry'][shape_file.first_valid_index()]
    
    mask=np.zeros([ni,nj])
    
    au=shapely.geometry.box(0,0,XCELL,XCELL,ccw=True)
    cell_area=au.area
    
       
    for i in range(0,ni):
        for j in range(0,nj):
            
            
            x=j*XCELL+XORIG
            y=i*XCELL+YORIG
                        
            pol=shapely.geometry.box(x,y,x+XCELL,y+XCELL,ccw=True)
            
            if pol.intersects(geometry_of_mask) == True:
                                              
                                
               mask[i,j]=np.round(geometry_of_mask.intersection(pol).area/cell_area,2)
                        
                      
           
        
    np.save('{0}/{1}'.format(output_dir,name),1-mask)  
            
       
        
    print("mask {0} is prepared in {1:.3f} seconds".format(name,time.time() - start_time))
    
    

    
    
    
    
    
    
    
    
    
    
    
    
