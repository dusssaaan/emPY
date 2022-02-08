d={}

# TNO bez SK, plosne

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
'filter':["ISO3 != 'SVK'"],
'EPSG':4326,
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2, BZN=0.016*NMVOC, NMBVOC=NMVOC-BZN',
'def_emis':{'NO2': 'NO2', 'NO': 'NO','BZN':'BZN','CO': 'CO', 'SO2': 'SO2', 'PM_CRS': 'PMC', 'PM2_5_EC': 'PEC', 'PM2_5_OC': 'POC', 'PM2_5_NA': 'PNA', 'PM2_5_SO4': 'PSO4', 'PM2_5_OTHR': 'PMOTHR', 'NBMVOC': 'NMBVOC', 'CH4': 'CH4', 'NH3': 'NH3'},
'emission_inventory':{1: 1010, 2: 1020, 34: 1040, 5: 1050, 6: 1060, 71: 1071, 72: 1072, 73: 1073, 74: 1074, 75: 1075, 8: 1080, 9: 1090, 10: 1100},
'units':'tonne/year',
 }

# TNO bez SK, bodove

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
'filter':["ISO3 != 'SVK'"],
'EPSG':4326,
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2, BZN=0.016*NMVOC, NMBVOC=NMVOC-BZN',
'def_emis':{'NO2': 'NO2', 'NO': 'NO','BZN':'BZN','CO': 'CO', 'SO2': 'SO2', 'PM_CRS': 'PMC', 'PM2_5_EC': 'PEC', 'PM2_5_OC': 'POC', 'PM2_5_NA': 'PNA', 'PM2_5_SO4': 'PSO4', 'PM2_5_OTHR': 'PMOTHR', 'NBMVOC': 'NMBVOC', 'CH4': 'CH4', 'NH3': 'NH3'},
'emission_inventory':{1: 1010, 34: 1040, 5: 1050, 8: 1080, 9: 1090, 10: 1100},
'units':'tonne/year',
 }

# polnohosp. emisie
# plosne
d['pol_v1']={
'source_type':'A',
'type':'csv',
'input_file':'/data/dusan/emPY/data/input/modelovanie_2019/polnohosp_plosne_uniform',
'sep':',',
'encoding':'utf-8',
'one_cat':2100,
'x':'x',
'y':'y',
'grid_dx':100,
'grid_dy':100,
'EPSG':3035,
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2, BZN=0.016*NMVOC, NMBVOC=NMVOC-BZN,PMC=PM10-PM2_5',
'def_emis':{'NH3': 'NH3', 'NMVOC': 'NMVOC','NOX':'NOX','PM25': 'PM2_5','PM10': 'PM10','CH4': 'CH4','CO': 'CO' },
'units':'tonne/year',
 }
# ako body druzstva
d['pol_point']={
'source_type':'P',
'type':'shape',
'one_cat':2100,
'def_heights':'zero',
'shape_file':'/data/dusan/emPY/data/input/modelovanie_2019/polnohosp_zbgis/zbgis_emisie.shp',
'def_emis':{'NH3': 'NH3', 'NMVOC': 'NMVOC','NOX':'NOX','PM25': 'PM2_5','PM10': 'PM10','CH4': 'CH4','CO': 'CO' },
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2, BZN=0.016*NMVOC, NMBVOC=NMVOC-BZN,PMC=PM10-PM2_5',
'units':'tonne/year',
 }
# kominy od janky

d['kominy_v1']={
'source_type':'P',
'type':'csv',
'input_file':'/data/dusan/emPY/data/input/modelovanie_2019/kominy_cmaq_v1',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'lon',
'y':'lat',
'def_heights':True,
'ID': 'ID',
'EPSG':4326,
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2,PMC=PM10-PM2_5',
'def_emis':{'nox(t)': 'NOX','benzen(t)':'BZN','co(t)': 'CO', 'so2(t)': 'SO2', 'PM10 (t)': 'PM10','PM2,5 (t)': 'PM2_5', 'nmvoc (t)': 'NMBVOC'},
'emission_inventory':{1: 2010,2: 2020, 3: 2030, 4:2040, 5: 2050, 6: 2060, 9: 2090},
'units':'tonne/year',
'height': 'stack heigh(m)',
'diameter': 'stack diameter',
'temperature': 'temperature (°C)',
'velocity': 'velocity of exhause gas(m/s)',
 }




d['kom_plosne_dupl']={
'source_type':'P',
'type':'csv',
'input_file':'/data/dusan/emPY/data/input/modelovanie_2019/kominy_cmaq_v1',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'lon',
'y':'lat',
'def_heights':'zero',
'ID': 'ID',
'EPSG':4326,
'new_pollutants':'NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2,PMC=PM10-PM2_5',
'def_emis':{'nox(t)': 'NOX','benzen(t)':'BZN','co(t)': 'CO', 'so2(t)': 'SO2', 'PM10 (t)': 'PM10','PM2,5 (t)': 'PM2_5', 'nmvoc (t)': 'NMBVOC'},
'emission_inventory':{1: 2010,2: 2020, 3: 2030, 4:2040, 5: 2050, 6: 2060, 9: 2090},
'units':'tonne/year',
'height': 'stack heigh(m)',
'diameter': 'stack diameter',
'temperature': 'temperature (°C)',
'velocity': 'velocity of exhause gas(m/s)',
 }







# CDV

d['cesty']={
'source_type':'L',
'shape_file':'/data/oko/other/ZBGIS_DMR35/roads_intensity/roads.shp',
'one_cat':2070,
'def_emis':{'intenzita': 'INZ'},
'units':'tonne/year',
}

d['CDV_faza2']={
'source_type':'L',
'shape_file':'/data/dusan/cdv_proc/shape_doprv_zjed_2020_faza2_opr/shape_doprv_zjed_2020_faza2_opr.shp',
'one_cat':2070,
'def_emis':{'BaP': 'BAP','NO2':'NO2', 'NO':'NO', 'PM10':'PM10','PM2':'PM2_5','Benzen':'BZN','SO2':'SO2','NMVOC':'NMVOC', 'NH3':'NH3','CO':'CO'},
'new_pollutants':'CH4=0.06*NMVOC, NMBVOC=NMVOC-CH4, PMC = PM10 - PM2_5',
'units':'kg/year',
}



d['CDV_2019_new']={
'source_type':'L',
'shape_file':'/data/dusan/emPY/data/input/modelovanie_2019/shape_doprv_zjed_2020/shape_doprv_zjed_2020.shp',
'one_cat':2070,
'def_emis':{'BaP': 'BAP','NO2':'NO2', 'NO':'NO', 'PM10':'PM10','PM2':'PM2_5','Benzen':'BZN','SO2':'SO2','NMVOC':'NMVOC', 'NH3':'NH3','CO':'CO'},
'new_pollutants':'CH4=0.06*NMVOC, NMBVOC=NMVOC-CH4, PMC = PM10 - PM2_5',
'units':'kg/year',
}



# kureniska

d['SVK_resHeat_15_85']={
'source_type':'A',
'type':'csv+shape',
'input_file':'/data/em/data/input/Slovakia/emiss_2015/res_heat/zsj_N15-L85/SK_2015_resHeat_N15-L85_all_fuels_NA_SO4_FPRM.csv',
'shape_file':'/data/em/data/input/Slovakia/geom/Slovakia_zastavane2.shp',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SRC_TYPE',
'source_id':'ZSJ',
'shape_id':'ZSJ_ID',
'def_emis':{'SO2_g': 'SO2', 'NH3_g': 'NH3', 'CH4_g': 'CH4', 'CO_g': 'CO', 'NOX_g': 'NOX', 'NMVOC_g': 'NMVOC', 'C6H6_g': 'BZN', 'BAP_mg': 'BAP', 'PM10_g': 'PM10', 'PM2_5_g': 'PM2_5', 'BC_g': 'PEC', 'OC_g': 'POC', 'NA_g': 'PNA', 'SO4_g': 'PSO4'},
'new_pollutants':'NMBVOC=NMVOC-CH4-BZN, PMC = PM10 - PM2_5, PMOTHR = PM2_5-PEC-POC-PNA-PSO4,NO2= 0.05*NOX, NO= 0.652*NOX-0.652*NO2',
'emission_inventory':{202020101: 2021, 2020202: 2022, 202020301: 2023, 202020302: 2023, 202020303: 2023, 202020304: 2023, 202020401: 2024},
'units':'g/year',
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

polu2 = ['NO_OA', 'NO_NL', 'NO_NT', 'NO_BUS', 'NO2_OA', 'NO2_NL',
       'NO2_NT', 'NO2_BUS', 'PM10_OA', 'PM10_NT', 'PM10_NL', 'PM10_BUS',
       'PM10_Resus', 'PM2_5_OA', 'PM2_5_NL', 'PM2_5_NT', 'PM2_5_BUS',
       'PM2_5_Resu', 'Benzen_OA', 'Benzen_NL', 'Benzen_NT', 'Benzen_BUS',
       'BaP_OA', 'BaP_NL', 'BaP_NT', 'BaP_BUS', 'BaP_Resus', 'SO2_OA',
       'SO2_NL', 'SO2_NT', 'SO2_BUS', 'N2O_OA', 'N2O_NL', 'N2O_NT', 'N2O_BUS',
       'Pb_OA', 'Pb_NL', 'Pb_NT', 'Pb_BUS', 'Cd_OA', 'Cd_NL', 'Cd_NT',
       'Cd_BUS', 'Ni_OA', 'Ni_NL', 'Ni_NT', 'Ni_BUS', 'As_OA', 'As_NL',
       'As_NT', 'As_BUS', 'Hg_OA', 'Hg_NL', 'Hg_NT', 'Hg_BUS']


d['CDV_2019_01_TN']={
'source_type':'L',
'shape_file':'/data/oko/EMISIE_CDV/etapa2/SHP/' + '01_Trencin/Trencin_EmisniToky_upr.shp',
'one_cat':1077,
'def_emis':{i:i for i in polu2},
'units':'tonne/year',
}

d['CDV_2019_02_BA']={
'source_type':'L',
'shape_file':'/data/oko/EMISIE_CDV/etapa2/SHP/' + '02_Bratislava/Bratislava_EmisniToky_upr.shp',
'one_cat':1077,
'def_emis':{i:i for i in polu2},
'units':'tonne/year',
}

d['CDV_2019_03_NR']={
'source_type':'L',
'shape_file':'/data/oko/EMISIE_CDV/etapa2/SHP/' + '03_Nitra/Nitra_EmisniToky_upr.shp',
'one_cat':1077,
'def_emis':{i:i for i in polu2},
'units':'tonne/year',
}

d['CDV_2019_04_MT']={
'source_type':'L',
'shape_file':'/data/oko/EMISIE_CDV/etapa2/SHP/' + '04_Martin/Martin_EmisniToky_upr.shp',
'one_cat':1077,
'def_emis':{i:i for i in polu2},
'units':'tonne/year',
}

d['CDV_2019_05_PO']={
'source_type':'L',
'shape_file':'/data/oko/EMISIE_CDV/etapa2/SHP/' + '05_Presov/Presov_EmisniToky_upr.shp',
'one_cat':1077,
'def_emis':{i:i for i in polu2},
'units':'tonne/year',
}

d['CDV_2019_06_ZA']={
'source_type':'L',
'shape_file':'/data/oko/EMISIE_CDV/etapa2/SHP/' + '06_Zilina/Zilina_EmisniToky_upr.shp',
'one_cat':1077,
'def_emis':{i:i for i in polu2},
'units':'tonne/year',
}

d['CDV_2019_07_KE']={
'source_type':'L',
'shape_file':'/data/oko/EMISIE_CDV/etapa2/SHP/' + '07_Kosice/Kosice_EmisniToky_upr.shp',
'one_cat':1077,
'def_emis':{i:i for i in polu2},
'units':'tonne/year',
}
















