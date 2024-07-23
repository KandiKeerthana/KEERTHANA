# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:40:48 2024

@author: hi
"""

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input()) 
for i in range(n):
    print(fib(i))   