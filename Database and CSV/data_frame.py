#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 08:45:08 2019

@author: suryanshshukla
"""

import pandas as pd
import matplotlib.pyplot as plt
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
    import statistics as st
    return st.mean(lst)


"""
Input the database of student
"""
name = []
enr = []
mar1 = []
mar2 = []
mar3 = []
mar4 = []
#
stu_len = int(input("Enter Length of databast"))
for j in range(stu_len):
    print("*******For", j+1, "Student*******")
    name.append(input('Name of student\n'))
    enr.append(input("Enrollment number \n"))
    mar1.append(float((input("1st Semester SGPA\n"))))
    mar2.append(float((input("2st Semester SGPA\n"))))
    mar3.append(float((input("3st Semester SGPA\n"))))
    mar4.append(float((input("4st Semester SGPA\n"))))
#Databaset of student

data = {'Enrollment' : enr, 'Name': name,
        'SGPA1': mar1,
        'SGPA2': mar2 ,
        'SGPA3': mar3,
        'SGPA4': mar4
        
        }
#to construct database using panda
df = pd.DataFrame(data)

##Saving the database to a file
df.to_csv('file1.csv')

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

##Calculating cgpa of 0 student
#marks = cgpa(data,0)
#print(AVG(marks))
df = df.set_index('Name')
print(df)


##Calculating the average CGPA in a class
print("cgpa list is", cal_cgpa())
