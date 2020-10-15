#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:39:28 2019

@author: suryanshshukla
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('file2.csv',index_col = 'Enrollment')
df = pd.DataFrame(data)

"""
This method returns the value contained in variable of dictionary
"""
def SGPA1_list(dicti):
    lst1 = dicti['SGPA1']
#    print(lst1)
    return lst1 
def SGPA2_list(dicti):
    lst2 = dicti['SGPA2']
    return lst2 
def SGPA3_list(dicti):
    lst3 = dicti['SGPA3']
    return lst3 
def SGPA4_list(dicti):
    lst4 = dicti['SGPA4']
    return lst4 

"""
Input = dictionary which is data and student number
OUTPUT = marks of given student in a list
calculating the cgpa of first student
"""
def cgpa(dicti,ID):
    sem1 = SGPA1_list(dicti)
    sem2 = SGPA2_list(dicti)
    sem3 = SGPA3_list(dicti)
    sem4 = SGPA4_list(dicti)
    
    stu = []
    stu.append(sem1[ID])
    stu.append(sem2[ID])
    stu.append(sem3[ID])
    stu.append(sem4[ID])
    
    return stu
"""
Input = list of SGPA of a given student
OUTPUT = AVERAGE of SGPA i.e. CGPA 
"""
def AVG(lst):

    return st.mean(lst)


"""
This method returns the value contained in variable of dictionary
"""
def SGPA1_list(dicti):
    lst1 = dicti['SGPA1']
#    print(lst1)
    return lst1 
def SGPA2_list(dicti):
    lst2 = dicti['SGPA2']
    return lst2 
def SGPA3_list(dicti):
    lst3 = dicti['SGPA3']
    return lst3 
def SGPA4_list(dicti):
    lst4 = dicti['SGPA4']
    return lst4 


"""
this function gives a list of average sgpa
"""
def cal_cgpa():
    lst5 = []
    for i in range(stu_len):
        a = cgpa(data,i)
        b = AVG(a)
        lst5.append(b)
    return (lst5)
#Adding the cgpa to the databse df
df['CGPA'] = cal_cgpa()





df = df.set_index('Name')
print(df)


##Calculating the average CGPA in a class
#print("cgpa list is", cal_cgpa())

avg_class = st.mean(cal_cgpa())

print("Abverage of class = ",avg_class)
#Year wise graph of CGPA of each student
df.plot.bar()
#df.plot.bar()
#df.plot.box()
#plt.figimage
