#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:40:02 2020

@author: student
"""


import pandas as pd


data_cal = pd.read_csv('/Users/student/Desktop/Nutrition-Summary-2020-01-01-to-2020-11-04.csv')
data_weight = pd.read_csv('/Users/student/Desktop/Measurement-Summary-2020-01-01-to-2020-11-04.csv')

# 

dic = dict()
for i in range(0,len(data_cal['Date'])-1):
    if data_cal['Date'][i] == data_cal['Date'][i+1]:
        if data_cal['Date'][i] not in dic.keys():
            dic[data_cal['Date'][i]] = int(data_cal['Calories'][i]) + int(data_cal['Calories'][i+1])
            
        else:
            dic[data_cal['Date'][i]] += int(data_cal['Calories'][i+1])
    
    elif data_cal['Date'][i] not in dic.keys():
        dic[data_cal['Date'][i]] = int(data_cal['Calories'][i])