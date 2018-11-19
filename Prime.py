# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:32:27 2018

@author: User
"""

x=int(input('Enter a number greater than 1:'))
for i in range(2,x):
  if (x%i)==0:
          print('Number is not prime')
          break
      
else:
          print('Number is prime')
      