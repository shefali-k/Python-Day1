# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:21:02 2018

@author: User
"""

def cel_far(x):
    return x*1.8 + 32
def far_cel(x):
    return (x-32)/1.8

a=float(input('Enter the temperature you want to convert: '))
b=int(input('Enter the operation to be performed: 1. Celsius to fahrenheit  2. Fahrenheit to celsius'))

if b==1:
    print(cel_far(a))
elif b==2:
    print(far_cel(a))
else:
    print('invalid operation')