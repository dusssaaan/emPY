"""
set the parameters for the emPY scripts
"""


##############################
#general settings

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

# set grid parameters
grid_params={'XCELL': 4710.621094,
 'XORIG': -426051.625,
 'YORIG': 110832.765625,
 'ni': 103,
 'nj': 184 }

#d03
#grid_params={'XCELL': 1570.20703125,
# 'XORIG': -14657.3125,
# 'YORIG': 159509.234375,
# 'ni': 142,
# 'nj': 271,
# 'nlays':7
#     }

# set grid params
#grid_params={'XCELL': 14131.86328125,
# 'XORIG': -1335201.875,
# 'YORIG': -685262.6875,
# 'ni': 133,
# 'nj': 169,
# 'nlays':7
#     }


##############################
#settings for to_domain

# import inventory inputs
import inventory_input as inventory_input

# import dictionary from inventory input
dic_inv=inventory_input.d

#list of inventory inputs which you want to take in the domain
#uncoment if you want all  
#list_inv=dic_inv.keys()
# or take just specific ones in list
#list_inv=['kominy_v1']
#list_inv=['EMEP_NOX','EMEP_BAP','EMEP_SOX','EMEP_PM25','EMEP_PM10']
list_inv=['TNO_SK_2015_P']
#define outpu directory of the to domain
to_domain_output_directory='/data/dusan/emPY/data/outputs-to_domain-2019_d02'

#set True if you want to have regriding control check in output
check_regrid=True #False

#set mask out file for the area sources which can be creating using the mask_out tool in tools 
#mask_area='/data/em/data/input/mask/SL_MP_BIG.npy'

#set shape file for masking out the point sources
#mask_point='/data/em/data/input/mask/silesia_and_malopolska_common_boundary.shp'

#parameters for the stacks which do not contain parameters in the invetory input
#this default parameters will be use.
parameters = {}
parameters[1010] = ('SO2', {31.69: {'height': 176.1, 'temperature': 368.4, 'velocity': 12.5, 'diameter': 6.8},
                                0.03: {'height': 125.9, 'temperature': 401.2, 'velocity': 10.4, 'diameter': 4.1},
                                   0: {'height':  33.3, 'temperature': 470.7, 'velocity':  8.2, 'diameter': 1.4}})
parameters[1030] = ('SO2', {3.169: {'height': 111.2, 'temperature': 417.1, 'velocity': 10.7, 'diameter': 3.5},
                              0.3169: {'height':  53.3, 'temperature': 458.7, 'velocity': 11.1, 'diameter': 2.0},
                                   0: {'height':  36.2, 'temperature': 412.0, 'velocity':  9.5, 'diameter': 1.9}})
parameters[1034] = parameters[1030]
parameters[1040] = ('CO',  {3.169: {'height':  39.0, 'temperature': 365.0, 'velocity': 10.4, 'diameter': 2.3},
                                0.03: {'height':  30.6, 'temperature': 396.4, 'velocity': 11.5, 'diameter': 1.5},
                                   0: {'height':  22.6, 'temperature': 435.8, 'velocity':  8.9, 'diameter': 1.3}})
parameters[1050] = ('CH4', {0.3169: {'height':  27.7, 'temperature': 344.0, 'velocity':  1.7, 'diameter': 3.1},
                          0.000000317: {'height':  17.0, 'temperature': 301.3, 'velocity':  7.6, 'diameter': 1.5},
                                    0: {'height':  11.0, 'temperature': 307.7, 'velocity':  8.1, 'diameter': 0.9}})
parameters[1060] = ('NMVOC',{0.3169: {'height':  16.1, 'temperature': 298.8, 'velocity':  9.1, 'diameter': 1.3},
                                 0.003: {'height':  11.0, 'temperature': 307.7, 'velocity':  8.1, 'diameter': 0.9},
                                     0: {'height':  13.6, 'temperature': 347.2, 'velocity':  7.0, 'diameter': 0.9}})
parameters[1090] = ('PM10', {0.3169: {'height': 126.2, 'temperature': 398.1, 'velocity': 11.8, 'diameter': 2.2},
                                  0.03: {'height':  39.7, 'temperature': 402.3, 'velocity':  9.0, 'diameter': 1.6},
                                     0: {'height':  22.5, 'temperature': 391.2, 'velocity':  8.1, 'diameter': 1.2}})

parameters[1100]=parameters[1050]
parameters[1080]=parameters[1040]

##############################
#setting for speciate

#####
#set input directory
speciate_input_dir='/data/dusan/emPY/data/outputs-to_domain-2019_d02'
# set the output directory
speciate_output_dir='/data/dusan/emPY/data/outputs-speciation-2019_d02_TNO'
# set the aero spec file
spec_file='/data/dusan/emPY/case_run/spec_file.csv'

#emission category file
em_cat_file='/data/dusan/emPY/case_run/emission_categories.csv'

#list inventory for area sources which you want if other than to domain make specific list
list_inv_area_spec=['TNO_SK_2015_A']

#list inventory for point sources which you want if other than to domain make specific list
list_inv_point_spec=['TNO_SK_2015_P']


##############################
#setting for time_variate
#set input directory
time_variate_input_dir='/data/dusan/emPY/data/outputs-speciation-2019_d02_TNO'
# set the output directory
time_variate_output_dir='/data/oko/dusan/emisie/modelovanie_2019/outputs-final-2019_d02_TNO'
#name of output files in form out_file_name-datum
out_file_name='EM_2019_d02_TNO'
#define main time ZONE of domain names must be recognized by library pytz
T_ZONE='Europe/Prague'
#time variate _mapping files 
tv_mapping='/data/dusan/emPY/case_run/tv_map_em.csv'
tv_values='/data/dusan/emPY/case_run/tv_values.csv'
#time variate _mapping files
tv_series='/data/dusan/emPY/case_run/tv_series.csv'
#start datum
datum_start='2017-01-02'
#end day
datum_end='2017-01-02'
#define dictionary output pollutants on cmaq input netcdf files, #only the names defined in this dictionary 
#and also in column spec_name will be in the final input
var_names={
'ACET': ['moles/s', 'ACET', 'Model species ACET'],
'ALD2': ['moles/s', 'ALD2', 'Model species ALD2'],
'ALD2_PRIMARY': ['moles/s', 'ALD2_PRIMARY', 'Model species ALD2_PRIMARY'],
'ALDX': ['moles/s', 'ALDX', 'Model species ALDX'],
'BAP': ['g/s', 'BAP', 'Model species BAP'],
'BENZ': ['moles/s', 'BENZ', 'Model species BENZ'],
'BENZENE': ['moles/s', 'BENZENE', 'Model species BENZENE'],
'CH4': ['moles/s', 'CH4', 'Model species CH4'],
'CO': ['moles/s', 'CO', 'Model species CO'],
'ETH': ['moles/s', 'ETH', 'Model species ETH'],
'ETHA': ['moles/s', 'ETHA', 'Model species ETHA'],
'ETHY': ['moles/s', 'ETHY', 'Model species ETHY'],
'ETOH': ['moles/s', 'ETOH', 'Model species ETOH'],
'FORM': ['moles/s', 'FORM', 'Model species FORM'],
'FORM_PRIMARY': ['moles/s', 'FORM_PRIMARY', 'Model species FORM_PRIMARY'],
'FACD': ['moles/s', 'FACD', 'Model species FACD'],
'HONO': ['moles/s', 'HONO', 'Model species HONO'],
'IOLE': ['moles/s', 'IOLE', 'Model species IOLE'],
'ISOP': ['moles/s', 'ISOP', 'Model species ISOP'],
'KET': ['moles/s', 'KET', 'Model species KET'],
'MEOH': ['moles/s', 'MEOH', 'Model species MEOH'],
'NAPH': ['moles/s', 'NAPH', 'Model species NAPH'],
'NH3': ['moles/s', 'NH3', 'Model species NH3'],
'NH3_FERT': ['moles/s', 'NH3_FERT', 'Model species NH3_FERT'],
'NO': ['moles/s', 'NO', 'Model species NO'],
'NO2': ['moles/s', 'NO2', 'Model species NO2'],
'NR': ['moles/s', 'NR', 'Model species NR'],
'NVOL': ['moles/s', 'NVOL', 'Model species NVOL'],
'OLE': ['moles/s', 'OLE', 'Model species OLE'],
'PAL': ['g/s', 'PAL', 'Model species PAL'],
'PAR': ['moles/s', 'PAR', 'Model species PAR'],
'PCA': ['g/s', 'PCA', 'Model species PCA'],
'PCL': ['g/s', 'PCL', 'Model species PCL'],
'PEC': ['g/s', 'PEC', 'Model species PEC'],
'PFE': ['g/s', 'PFE', 'Model species PFE'],
'PH2O': ['g/s', 'PH2O', 'Model species PH2O'],
'PK': ['g/s', 'PK', 'Model species PK'],
'PMC': ['g/s', 'PMC', 'Model species PMC'],
'PMFINE': ['g/s', 'PMFINE', 'Model species PMFINE'],
'PMG': ['g/s', 'PMG', 'Model species PMG'],
'PMN': ['g/s', 'PMN', 'Model species PMN'],
'PMOTHR': ['g/s', 'PMOTHR', 'Model species PMOTHR'],
'PNA': ['g/s', 'PNA', 'Model species PNA'],
'PNCOM': ['g/s', 'PNCOM', 'Model species PNCOM'],
'PNH4': ['g/s', 'PNH4', 'Model species PNH4'],
'PNO3': ['g/s', 'PNO3', 'Model species PNO3'],
'POC': ['g/s', 'POC', 'Model species POC'],
'PRPA': ['moles/s', 'PRPA', 'Model species PRPA'],
'PSI': ['g/s', 'PSI', 'Model species PSI'],
'PSO4': ['g/s', 'PSO4', 'Model species PSO4'],
'PTI': ['g/s', 'PTI', 'Model species PTI'],
'SO2': ['moles/s', 'SO2', 'Model species SO2'],
'SOAALK': ['moles/s', 'SOAALK', 'Model species SOAALK'],
'SULF': ['moles/s', 'SULF', 'Model species SULF'],
'TERP': ['moles/s', 'TERP', 'Model species TERP'],
'TOL': ['moles/s', 'TOL', 'Model species TOL'],
'UNK': ['moles/s', 'UNK', 'Model species UNK'],
'UNR': ['moles/s', 'UNR', 'Model species UNR'],
'VOC_INV': ['g/s', 'VOC_INV', 'Model species VOC_INV'],
'XYL': ['moles/s', 'XYL', 'Model species XYL'],
'XYLMN': ['moles/s', 'XYLMN', 'Model species XYLMN']}

