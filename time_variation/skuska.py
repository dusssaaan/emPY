#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:43:50 2021

@author: p6001
"""

import xarray as xr
import netCDF4
import pandas as pd

time_3D_arr = xr.open_dataset('/data/teri/sezonalita_kv_ovzd/time_profiles/res_heat_profile_HDD_13_hourly_TNO_solid.nc')


time_3D_arr_nc = netCDF4.Dataset('/data/teri/sezonalita_kv_ovzd/time_profiles/res_heat_profile_HDD_13_hourly_TNO_solid.nc')


#%%
import datetime 

datum_start=datetime.datetime(2017,1,1,0)

index = datum_start.timetuple().tm_yday*24+datum_start.timetuple().tm_hour

time_3D_mat=time_3D_arr_nc.variables['TimeProfile'][index:index+25,:,:].data

print(index) 

#%%
mat_a=np.array([[5,3],[4,6]])
mat_b=([1,2])

mat_a1=np.expand_dims(mat_a, axis=0)
mat_b=np.expand_dims(mat_a, axis=0)

np.multiply



















