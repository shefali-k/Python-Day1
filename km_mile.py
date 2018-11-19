# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:08:37 2018

@author: User
"""
def km_mile(x):
    return x*0.621
def mile_km(x):
    return x*1.609

a=float(input('Enter the distance you want to convert: '))
b=int(input('Enter the operation to be performed: 1. Km to mile  2. Mile to km'))

if b==1:
    print(km_mile(a))
elif b==2:
    print(mile_km(a))
else:
    print('invalid operation')