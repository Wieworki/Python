# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:38:15 2022

@author: Augusto
"""

def encrypt (text,num):
    ''' Caesar Cihper '''    
    #26 letters
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabet_len = len(alphabet)
    alphabet_to_values = {}
    values_to_alphabet = {}
    
    for i in range(len(alphabet)):
        alphabet_to_values[alphabet[i]] = i

    for i in range(len(alphabet)):
        values_to_alphabet[i] = alphabet[i]
    
    #Diccionario con los valores cifrados
    cyphered_text = {}
    
    for index,letter in enumerate(text):
        #En index recuperamos el indice
        #En letter, el valor de la lista en ese indice
        
        letter_value = alphabet_to_values[letter.upper()]
        new_value = letter_value+num
        if(new_value >= alphabet_len):
            new_value -= alphabet_len
        elif(new_value < 0):
            new_value += alphabet_len            
        cyphered_text[index] =  values_to_alphabet[newValue]
    return cyphered_text
