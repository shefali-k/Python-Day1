# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:21:40 2018

@author: User

"""
import cmath

a=float(input('enter the value of a in the quadratic equation:'))
b=float(input('enter the value of b in the quadratic equation:'))
c=float(input('enter the value of c in the quadratic equation:'))

d= (b*b)-(4*a*c)
ans = (-b+cmath.sqrt(d))/(2*a)
ans1= (-b-cmath.sqrt(d))/(2*a)

if d<0:
    print('imaginary roots')
elif d==0:
    print('equal roots: r1= '-b/2*a )
elif d>0:
    
    print("ans1:")
    print('ans2:')
