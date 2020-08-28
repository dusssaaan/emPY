#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calculate missing pollutants
"""

import pandas as pd
import numpy as np
import os

def cal_pol(output_dir,calculate_pol_file):
    
    cal_pol_file=pd.read_csv(calculate_pol_file, sep=',')
    
    
    cat_em_list=[]
    
    for file in os.listdir('{0}'.format(output_dir)):
            
            f_split=file.split( "-" )
            cat_em='{0}-{1}'.format(f_split[0],f_split[1])
            cat_em_list.append(cat_em)
     
    name=f_split[2]
    
    categories_presented=[]
    for i in cat_em_list:
        i=i.split('-')
        categories_presented.append(int(i[0]))
        
    
    for index, cal in cal_pol_file.iterrows():
        cat=cal[cal_pol_file.columns[0]]
        #!!!!!!!!!!!!!!!!
        if cat  in categories_presented:
            #print(cat)
            l=cal['expression'].split(',')
            #print(l)
            for ex in l:
                ex=ex.split('=')
                pol_orig=ex[0].strip()
                exp=ex[1]
                if '-' in exp:
                    exp2=exp.split('-')
                    if '*' in exp2[0]:
                       exp3=exp2[0].split('*') 
                       coef1=float(exp3[0])
                       pol1=exp3[1]
                    else:
                       coef1=1.0
                       pol1=exp2[0]
                    if '*' in exp2[1]:
                       exp3=exp2[1].split('*') 
                       coef2=float(exp3[0])
                       pol2=exp3[1]
                    else:
                       coef2=1.0
                       pol2=exp2[1]
                    
                    if '{0}-{1}'.format(cat,pol_orig) not in cat_em_list:
                       
                       print('##### calculate pollutants')
                       print('{0}-{1} is not in inventory'.format(cat,pol_orig))
                       print('Equation is {4}={0}*{1}-{2}*{3} used'.format(coef1,pol1,coef2,pol2,pol_orig))
                                       
                        
                       try: 
                           pol1np=np.load('{0}/{1}-{2}-{3}'.format(output_dir,cat,pol1,name))
                           pol2np=np.load('{0}/{1}-{2}-{3}'.format(output_dir,cat,pol2,name))
                           
                           polnew=coef1*pol1np-coef2*pol2np
                           np.save('{0}/{1}-{2}-{3}'.format(output_dir,cat,pol_orig,name),polnew)
                           
                       except FileNotFoundError:
                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                           print('{0}-{1} or {0}-{2} are not in inventory'.format(cat,pol1,pol2))
                    
                       
                elif '+' in exp:
                    exp2=exp.split('+')
                    if '*' in exp2[0]:
                       exp3=exp2[0].split('*') 
                       coef1=float(exp3[0])
                       pol1=exp3[1]
                    else:
                       coef1=1.0
                       pol1=exp2[0]
                    if '*' in exp2[1]:
                       exp3=exp2[1].split('*') 
                       coef2=float(exp3[0])
                       pol2=exp3[1]
                    else:
                       coef2=1.0
                       pol2=exp2[1] 
                    
                    if '{0}-{1}'.format(cat,pol_orig) not in cat_em_list:
                       
                       print('##### calculate pollutants')
                       print('{0}-{1} is not in inventory'.format(cat,pol_orig))
                       print('Equation is {4}={0}*{1}+{2}*{3} used'.format(coef1,pol1,coef2,pol2,pol_orig))
                 
                        
                       try: 
                           pol1np=np.load('{0}/{1}-{2}-{3}'.format(output_dir,cat,pol1,name))
                           pol2np=np.load('{0}/{1}-{2}-{3}'.format(output_dir,cat,pol2,name))
                           polnew=coef1*pol1np+coef2*pol2np
                           np.save('{0}/{1}-{2}-{3}'.format(output_dir,cat,pol_orig,name),polnew)
                       
                       except FileNotFoundError:
                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                           print('{0}-{1} or {0}-{2} are not in inventory'.format(cat,pol1,pol2))
                    
                       
                       
                    
                else:
                    if '*' in exp:
                       exp3=exp.split('*') 
                       coef1=float(exp3[0])
                       pol1=exp3[1]
                    else:
                       coef1=1.0
                       pol1=exp
                       
                    if '{0}-{1}'.format(cat,pol_orig) not in cat_em_list:
                       
                       print('##### calculate pollutants')
                       print('{0}-{1} is not in inventory'.format(cat,pol_orig))
                       print('Equation is {2}={0}*{1} used'.format(coef1,pol1,pol_orig))
                    
                       
                       
                       
                       try:
                           pol1np=np.load('{0}/{1}-{2}-{3}'.format(output_dir,cat,pol1,name))
                           polnew=coef1*pol1np
                           np.save('{0}/{1}-{2}-{3}'.format(output_dir,cat,pol_orig,name),polnew)
                       except FileNotFoundError:
                           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                           print('{0}-{1} is not in inventory'.format(cat,pol1))
                    
                       
                     
        
    
    