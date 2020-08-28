#!/usr/bin/env /data/juraj/anaconda3/envs/geo/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:09:49 2019

@author: p6001
"""

import os
import numpy as np


for subdir, dire, file in os.walk('/data/em/data/outputs-to_grid-d01-LifeIP-CMAQ_old/'):
    #print(subdir, file)
    pom=subdir.split('/')[-1]  
   
    if pom in os.listdir('/data/dusan/EMPYS/data/outputs_to_grid_skusanie/'):
        #print(pom)
        for files in file:
         
         if os.path.isfile('/data/dusan/EMPYS/data/outputs_to_grid_skusanie/'+pom+'/'+files): 
            a=np.load('/data/em/data/outputs-to_grid-d01-LifeIP-CMAQ_old/{0}/{1}'.format(str(pom),str(files)))
            b=np.load('/data/dusan/EMPYS/data/outputs_to_grid_skusanie/'+pom+'/'+files)
            if len(a.shape) == 3: 
               a=np.sum(a,axis=0) 
            
            if np.abs(np.sum(a-b)) > 0.0001:
                print(pom)
                print(files, np.sum(a-b))
                print(np.sum(a))
                print(np.sum(b))