#!/usr/bin/env /python
"""

MASK SCRIPT

Function:    
making mask according to the shapefile and save it into the numpy array

Libraries and modules needed:
libraries: 
modules:
src.mask_out    
containing function create_mask(shape_file, output_dir,name_of_mask, projection, grid_params)    
Revision History:
    
30.01.2019 D. Stefanik: creating first version of script


"""
# import module
import src_mask_out.mask_out as mask



# set projection
projection={'proj': 'lcc',
 'lat_1': 46.24470138549805,
 'lat_2': 46.24470138549805,
 'lat_0': 46.24470138549805,
 'lon_0': 17.0,
 'x_0': 0,
 'y_0': 0,
 'a': 6370000.0,
 'b': 6370000.0,
 'units': 'm',
 'no_defs': True}


# set grid params
grid_params={'XCELL': 4710.621094,
 'XORIG': -426051.625,
 'YORIG': 110832.765625,
 'ni': 103,
 'nj': 184,
 'nlays':7 
     }

#shape_file
shape_file='/data/dusan/test_katerina/silesia_and_malopolska_wgs84.shp'
#output_dir
output_dir='/data/em/data/input/mask'

#name of mask
name_of_mask='Sliezsko'

######run##############################
mask.create_mask(shape_file, output_dir,name_of_mask, projection, grid_params)
