# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:04:00 2018

@author: User
"""
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
x=float(input('Enter the FIRST number:'))
y=float(input('Enter the SECOND number:'))
c=int(input('Select the operation you want to perform: 1. Addition 2. Subtaction 3. Multiplication 4. Division:'))
if c==1:
    print(add(x,y))
elif c==2:
    print(sub(x,y))
elif c==3:
    print(mul(x,y))
elif c==4:
    print(div(x,y))
else:
    print('Invalid Operation')