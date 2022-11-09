# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:48:34 2022

@author: Augusto
"""

def insertion_sort(lista):
    largo = len(lista)
    for i in range(1,largo):
        valor = lista[i]        #Valor actual a comparar
        j = i                   #Indice del valor actual
        while j > 0 and lista[j-1] > valor: 
            #Asumimos que para atrás, la lista[0:i] ya tiene sus valores ordenados
            #La posicion de este elemento, sera la inmediatamente siguiente 
            #a la posicion del primer elemento que supere en valor
            lista[j] = lista[j-1]   #Corremos para la derecha el valor mayor
            j = j - 1
        lista[j] = valor
    return lista

x = insertion_sort([5,6,7,2,-1,9,15,0,3,5])
print(x)                
