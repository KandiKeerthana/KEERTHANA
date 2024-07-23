# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:49:56 2024

@author: hi
"""

def exp(base,pow):
    if pow==0:
        return 1
    else:
        return base*exp(base,pow-1)
base=int(input())
pow=int(input())
print(exp(base,pow))    