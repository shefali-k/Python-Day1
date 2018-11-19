# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:49:34 2018

@author: User
"""
def fibb (n):
    if n<=1:
        return n
    else:
        return(fibb(n-1)+fibb(n-2))
a=int(input('Enter the positive number upto which you want fibonacci series:'))

for i in range(a):
    print(fibb(i))