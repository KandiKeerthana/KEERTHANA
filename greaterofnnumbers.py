# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:38:19 2024

@author: hi
"""

a,b,c=map(int,input().split(" "))
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")    
    