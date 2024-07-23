# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:48:42 2024

@author: hi
"""

n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("its prime")
else:
    print("not")    