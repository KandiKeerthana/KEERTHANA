# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:47:00 2024

@author: hi
"""

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input()) 
print(fact(n))   