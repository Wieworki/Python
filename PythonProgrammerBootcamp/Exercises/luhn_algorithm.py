# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:57:46 2022

@author: Augusto
"""

def luhn_algorithm(credit_number):
    ''' Credit card validation algorithm '''
    #First step: Multiply every 2nd digit by 2 starting from the 2nd to last
    #and add those digits together
    
    suma = 0
    index_multiply = False
    for i in reversed(credit_number):
        if index_multiply: 
            decena = (i*2) // 10  #Floor division, 0 if < 10
            unidad = (i*2) % 10   #Resto
            suma += decena
            suma += unidad
            index_multiply = False
        else:
            index_multiply = True
    #Second step: Add those numbers to the sum of the digits that
    #where not mutiplied by 2   
    index_sum = True
    for i in reversed(credit_number):
        if index_sum:
            suma += i
            index_sum = False
        else:
            index_sum = True
    #Third step: Find the reminder when that result is divided by 10
    #If the reminder is 0, the number is valid
    
    return suma % 10 == 0

print(luhn_algorithm([3,7,1,4,4,9,6,3,5,3,9,8,4,3,1]))
