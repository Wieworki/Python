# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:12:11 2022

@author: Augusto
"""

from random import choice
import matplotlib.pyplot as plt

def random_walk(steps):
    step_option = [1,-1]                #Opciones disponibles
    step_choice = choice(step_option)   #Usamos la libreria para elegir una al azar
    walk = []
    walk.append(step_choice)
    for step in range(1,steps):
        next_step = walk[step-1] + choice(step_option)
        walk.append(next_step)
    return walk

#Cambiamos las opciones de configuracios del grafico
plt.rc('figure',figsize=(12,6))
plt.title('Walk plot 1')      #Titulo
plt.xlabel('Step number')   #Leyenda eje horizontal
plt.ylabel('Direction')     #Leyenda eje vertical

#Primer grafico
walk1 = random_walk(100)
plt.plot(walk1,'ko--',label='Plot 1')   #Con label establecemos asignamos un nombre para la leyenda
plt.legend(loc='lower left')            #Luego de crear el grafico, indicamos donde ira la leyenda

#Segundo grafico
walk2 = random_walk(100)
plt.plot(walk2,label = 'Plot 2')
plt.legend(loc='lower left')    

plt.show()
