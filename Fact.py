# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:21:40 2018

@author: User
"""
fact=1
x=int(input('Enter the number to find its factorial:'))
if x<0:
    print('factorial does not exist')
elif x==0:
    print('Factorial of zero is 1')
else:
    for i in range(1,x+1):
      fact=fact*i
    print(fact)