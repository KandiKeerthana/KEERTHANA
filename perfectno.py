# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:15:41 2024

@author: hi
"""

n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print("perfect no")
else:
    print("not")       