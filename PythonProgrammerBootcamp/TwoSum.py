# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:08:43 2022

@author: Augusto
"""


def two_sum(lista,targetSum):
    ''' Dada una lista de numeros, devolver el indice de los dos valores que sumados
    dan como resultado el valor objetivo. Devuelve -1 -1 si no encuentra'''
    for index,value in enumerate(lista):
        valorActual = lista[index]
        valorBuscado = targetSum - valorActual
        if valorBuscado in lista:
            ubicacion = lista.index(valorBuscado)
            return [index,ubicacion]
    return [-1,-1]
