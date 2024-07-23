# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:57:00 2024

@author: hi
"""

def son(n):
    if n==0:
        return 0
    else:
        return n+son(n-1)
n=int(input())
print(son(n))    