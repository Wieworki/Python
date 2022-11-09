# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:44:31 2022

@author: Augusto
"""

def linear_search(lista,target):
    for index,elem in enumerate(lista):
        if elem == target:
            return index
    return -1

x = linear_search([1,2,3,4,5],2)
print(x)

