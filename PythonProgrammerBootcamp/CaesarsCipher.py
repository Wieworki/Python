# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:38:15 2022

@author: Augusto
"""

def encrypt (text,num):
    ''' Caesar Cihper '''    
    #26 letters
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabetLen = len(alphabet)
    alphabetToValues = {}
    valuesToAlphabet = {}
    
    for i in range(len(alphabet)):
        alphabetToValues[alphabet[i]] = i

    for i in range(len(alphabet)):
        valuesToAlphabet[i] = alphabet[i]
    
    #Diccionario con los valores cifrados
    cypheredText = {}
    
    for index,letter in enumerate(text):
        #En index recuperamos el indice
        #En letter, el valor de la lista en ese indice
        
        letterValue = alphabetToValues[letter.upper()]
        newValue = letterValue+num
        if(newValue >= alphabetLen):
            newValue -= alphabetLen
        elif(newValue < 0):
            newValue += alphabetLen            
        cypheredText[index] =  valuesToAlphabet[newValue]
    return cypheredText
