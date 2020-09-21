d={}

d['TNO_SK_2015_A']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input'+'/TNO/TNO_2015_A',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'Lon',
'y':'Lat',
'grid_dx':0.125,
'grid_dy':0.0625,
'filter':["ISO3 == 'SVK'"],
'EPSG':4326,
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2, BZN=0.016*NMVOC, NMBVOC=NMVOC-BZN',
'def_emis':{'NO2': 'NO2', 'NO': 'NO','BZN':'BZN','CO': 'CO', 'SO2': 'SO2', 'PM_CRS': 'PMC', 'PM2_5_EC': 'PEC', 'PM2_5_OC': 'POC', 'PM2_5_NA': 'PNA', 'PM2_5_SO4': 'PSO4', 'PM2_5_OTHR': 'PMOTHR', 'NBMVOC': 'NMBVOC', 'CH4': 'CH4', 'NH3': 'NH3'},
'emission_inventory':{1: 1010, 2: 1020, 34: 1040, 5: 1050, 6: 1060, 71: 1071, 72: 1072, 73: 1073, 74: 1074, 75: 1075, 8: 1080, 9: 1090, 10: 1100},
'units':'tonne/year',
 }


d['TNO_SK_2015_P']={
'source_type':'P',
'type':'csv',
'input_file':'/data/em/data/input'+'/TNO/TNO_2015_P',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'Lon',
'y':'Lat',
'def_heights':False,
'ID': 'ID',
'filter':["ISO3 == 'SVK'"],
'EPSG':4326,
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2, BZN=0.016*NMVOC, NMBVOC=NMVOC-BZN',
'def_emis':{'NO2': 'NO2', 'NO': 'NO','BZN':'BZN','CO': 'CO', 'SO2': 'SO2', 'PM_CRS': 'PMC', 'PM2_5_EC': 'PEC', 'PM2_5_OC': 'POC', 'PM2_5_NA': 'PNA', 'PM2_5_SO4': 'PSO4', 'PM2_5_OTHR': 'PMOTHR', 'NBMVOC': 'NMBVOC', 'CH4': 'CH4', 'NH3': 'NH3'},
'emission_inventory':{1: 1010, 34: 1040, 5: 1050, 8: 1080, 9: 1090, 10: 1100},
'units':'tonne/year',
 }
