# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:08:43 2022

@author: Augusto
"""


def two_sum(lista,target_sum):
    ''' Dada una lista de numeros, devolver el indice de los dos valores que sumados
    dan como resultado el valor objetivo. Devuelve -1 -1 si no encuentra'''
    for index,value in enumerate(lista):
        valor_actual = lista[index]
        valor_buscado = target_sum - valor_actual
        if valor_buscado in lista:
            ubicacion = lista.index(valor_buscado)
            return [index,ubicacion]
    return [-1,-1]
