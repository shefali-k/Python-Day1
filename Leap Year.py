# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:45:35 2018

@author: User
"""

year=int(input('enter the year you want to check:'))
if (year%4==0) or (year%400==0):
     print('year is a LEAP YEAR')   
else:
    print('year is NOT a LEAP YEAR')