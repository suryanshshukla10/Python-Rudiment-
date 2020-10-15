#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:47:36 2019

@author: suryanshshukla
"""

"""
Reading the database
"""

import enter_database_2 as database
import pandas as pd
import matplotlib.pyplot as plt
def read(*a):    
    flag = 'q'
    
    while flag != 'exit':
        #Input to view or edit database
        flag = input("Enter\n V = view existing dataset \n E = new database\n Type exit to terminate processs\n")
        if flag == 'exit' or flag == 'EXIT' or flag == 'Exit':
            break
        elif flag == 'E' or flag == 'e':
            
            y = database.runn.enter()
            
        elif flag == 'V' or  flag == 'v':
            data = pd.read_csv('file1.csv')
             data = data.set_index('Name') 
            print(data)
