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

d['pol_v1']={
'source_type':'A',
'type':'csv',
'input_file':'/data/dusan/pol_em/polem_emPY_v1',
'sep':',',
'encoding':'utf-8',
'one_cat':1100,
'x':'x',
'y':'y',
'grid_dx':100,
'grid_dy':100,
'EPSG':3035,
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2, BZN=0.016*NMVOC, NMBVOC=NMVOC-BZN',
'def_emis':{'NH3': 'NH3', 'NMVOC': 'NMVOC','NOX':'NOX','PM25': 'PM25','PM10': 'PM10','CH4': 'CH4','CO': 'CO' },
'units':'tonne/year',
 }

d['pol_point']={
'source_type':'P',
'type':'shape',
'one_cat':1100,
'def_heights':'zero',
'shape_file':'/data/dusan/pol_em/zbgis_emisie/zbgis_emisie.shp',
'def_emis':{'NH3': 'NH3', 'NMVOC': 'NMVOC','NOX':'NOX','PM25': 'PM25','PM10': 'PM10','CH4': 'CH4','CO': 'CO' },
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2, BZN=0.016*NMVOC, NMBVOC=NMVOC-BZN',
'units':'tonne/year',
 }


d['kominy_v1']={
'source_type':'P',
'type':'csv',
'input_file':'/data/dusan/emPY/data/input/kominy_cmaq_v1',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'lon',
'y':'lat',
'def_heights':True,
'ID': 'ID',
'EPSG':4326,
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2,PMC=PM_10-PM2_5',
'def_emis':{'nox(t)': 'NOX','benzen(t)':'BZN','co(t)': 'CO', 'so2(t)': 'SO2', 'PM10 (t)': 'PM_10','PM2,5 (t)': 'PM2_5', 'nmvoc (t)': 'NMBVOC'},
'emission_inventory':{1: 2010,2: 2020, 3: 2030, 4:2040, 5: 2050, 6: 2060, 9: 2090},
'units':'tonne/year',
'height': 'stack heigh(m)',
'diameter': 'stack diameter',
'temperature': 'temperature (°C)',
'velocity': 'velocity of exhause gas(m/s)',
 }



























polu=['NO_OV', 'NO_LNV', 'NO_TNV', 'NO_BUS', 'NO2_OV', 'NO2_LNV',
       'NO2_TNV', 'NO2_BUS', 'N2O_OV', 'N2O_LNV', 'N2O_TNV', 'N2O_BUS',
       'PM10_OV', 'PM10_LNV', 'PM10_TNV', 'PM10_BUS', 'PM10_Resus', 'PM2_5_OV',
       'PM2_5_LNV', 'PM2_5_TNV', 'PM2_5_BUS', 'PM2_5_Resu', 'Benzen_OV',
       'Benzen_LNV', 'Benzen_TNV', 'Benzen_BUS', 'BaP_OV', 'BaP_LNV',
       'BaP_TNV', 'BaP_BUS', 'BaP_Resusp', 'SO2_OV', 'SO2_LNV', 'SO2_TNV',
       'SO2_BUS', 'Pb_OV', 'Pb_LNV', 'Pb_TNV', 'Pb_BUS', 'Cd_OV', 'Cd_LNV',
       'Cd_TNV', 'Cd_BUS', 'Ni_OV', 'Ni_LNV', 'Ni_TNV', 'Ni_BUS', 'As_OV',
       'As_LNV', 'As_TNV', 'As_BUS', 'Hg_OV', 'Hg_LNV', 'Hg_TNV', 'Hg_BUS']


d['CDV_2019']={
'source_type':'L',
'shape_file':'/data/dusan/cdv_proc/shape_upr_1/shape_upr_1.shp',
'one_cat':1077,
'def_emis':{i:i for i in polu},
'units':'tonne/year',
}



d['CDV_2019_new']={
'source_type':'L',
'shape_file':'/data/dusan/cdv_proc/shape_doprv_zjed_2020/shape_doprv_zjed_2020.shp',
'one_cat':2070,
'def_emis':{'NO2':'NO2', 'NO':'NO', 'PM10':'PM10','PM2':'PM2_5','Benzen':'BENZ','SO2':'SO2','NMVOC':'NMVOC', 'NH3':'NH3','CO':'CO'},
'new_pollutants':'CH4=0.06*NMVOC, NMBVOC=NMVOC-CH4, PMC = PM10 - PM2',
'units':'tonne/year',
}





d['EMEP_NOX']={
'source_type':'A',
'type':'csv',
'input_file':'/data/dusan/EMEP_GRID_UPRAVA/'+'EMEP_NOX_GRID',
'sep':',',
'encoding':'utf-8',
'cat_internal':'category',
'x':'LONGITUDE',
'y':'LATITUDE',
'grid_dx':0.1,
'grid_dy':0.1,
'filter':["ISO2 == 'SK'"],
'EPSG':4326,
'def_emis':{'EMISSION': 'NOX'},
'units':'tonne/year',
'emission_inventory':{1:1, 2:2, 3:3, 4:4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,11:11,12:12,13:13,14:14}, 
}


d['EMEP_BAP']={
'source_type':'A',
'type':'csv',
'input_file':'/data/dusan/EMEP_GRID_UPRAVA/'+'EMEP_BAP_GRID',
'sep':',',
'encoding':'utf-8',
'cat_internal':'category',
'x':'LONGITUDE',
'y':'LATITUDE',
'grid_dx':0.1,
'grid_dy':0.1,
'filter':["ISO2 == 'SK'"],
'EPSG':4326,
'def_emis':{'EMISSION': 'BAP'},
'units':'tonne/year',
'emission_inventory':{1:1, 2:2, 3:3, 4:4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,11:11,12:12,13:13,14:14},
}

d['EMEP_PM10']={
'source_type':'A',
'type':'csv',
'input_file':'/data/dusan/EMEP_GRID_UPRAVA/'+'EMEP_PM10_GRID',
'sep':',',
'encoding':'utf-8',
'cat_internal':'category',
'x':'LONGITUDE',
'y':'LATITUDE',
'grid_dx':0.1,
'grid_dy':0.1,
'filter':["ISO2 == 'SK'"],
'EPSG':4326,
'def_emis':{'EMISSION': 'PM10'},
'units':'tonne/year',
'emission_inventory':{1:1, 2:2, 3:3, 4:4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,11:11,12:12,13:13,14:14},
}

d['EMEP_PM25']={
'source_type':'A',
'type':'csv',
'input_file':'/data/dusan/EMEP_GRID_UPRAVA/'+'EMEP_PM2,5_GRID',
'sep':',',
'encoding':'utf-8',
'cat_internal':'category',
'x':'LONGITUDE',
'y':'LATITUDE',
'grid_dx':0.1,
'grid_dy':0.1,
'filter':["ISO2 == 'SK'"],
'EPSG':4326,
'def_emis':{'EMISSION': 'PM25'},
'units':'tonne/year',
'emission_inventory':{1:1, 2:2, 3:3, 4:4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,11:11,12:12,13:13,14:14},
}


d['EMEP_SOX']={
'source_type':'A',
'type':'csv',
'input_file':'/data/dusan/EMEP_GRID_UPRAVA/'+'EMEP_SOX_GRID',
'sep':',',
'encoding':'utf-8',
'cat_internal':'category',
'x':'LONGITUDE',
'y':'LATITUDE',
'grid_dx':0.1,
'grid_dy':0.1,
'filter':["ISO2 == 'SK'"],
'EPSG':4326,
'def_emis':{'EMISSION': 'SOX'},
'units':'tonne/year',
'emission_inventory':{1:1, 2:2, 3:3, 4:4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,11:11,12:12,13:13,14:14},
}




