#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:08:37 2019

@author: p6001
"""
import subprocess
#path to python environment

python_path="/data/juraj/anaconda3/envs/geo/bin/python"

#path to current config file
home_path   = '/data/dusan/EMPYS'
config_path = home_path+'/case_run'


# run 
subprocess.call("{0} {1}/to_domain/run.py '{2}'".format(python_path,home_path,config_path), shell=True)





