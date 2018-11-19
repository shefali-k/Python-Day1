# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:03:10 2018

@author: User
"""

a=float(input('Enter first number'))
b=float(input('Enter second number'))
c=float(input('Enter third number'))
if a>b and a>c:
    print(a,'is largest')
elif b>a and b>c:
    print(b,'is largest')
else:
    print(c,'is largest')
    
    if a<b and a<c:
        print(a,'is smallest')
    elif b<a and b<c:
        print(b,'is smallest')
    else:
        print(c,'is smallest')
            
        