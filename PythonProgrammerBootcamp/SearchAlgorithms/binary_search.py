# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:53:56 2022

@author: Augusto
"""

def binary_search(lista,target):
    ''' La lista ya debe venir ordenada '''
    
    if len(lista) == 0:
        return -1
    if len(lista) == 1:
        if lista[0] == target:
            return 0
        else:
            return -1
        
    inicio = 0
    fin = len(lista)
    found = False
    middle = (fin + inicio) // 2
    while not found:
        if middle == fin or middle == inicio:
            #Quedan 2 o 1 elemento en la lista
            if lista[fin] == target:
                found = True
                return fin
            elif lista[inicio] == target:
                found = True
                return inicio
            else:
                #No se encuentra
                return -1
        middle = (fin + inicio) // 2
        if lista[middle] == target:
            found = True
            return middle
        elif lista[middle] > target:
            #print(f'{lista[middle]} mayor a {target}')
            fin = middle - 1
        else:
            #print(f'{lista[middle]} menor a {target}')
            inicio = middle + 1
            
        
    
x = binary_search([-1,0,1,2], 2)
print(x)
