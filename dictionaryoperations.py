# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:26:58 2024

@author: hi
"""

menu={
      'chicken_biryani':599,
      'butter_chicken':450,
      'tandoori_chicken':555,
      'juicy_mandi':700
      }
print(menu['butter_chicken'])
menu['fruits_salad']=750
print(menu)
menu['juicy _mandi']=777
print(menu)
menu.pop('chicken_biryani')
print(menu)