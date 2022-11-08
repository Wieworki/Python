# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:51:09 2022

@author: Augusto
"""

import matplotlib.pyplot as plt
import numpy as np


#Cambiamos las opciones de configuracios del plot
plt.rc('figure',figsize=(12,6))

values = list(range(0,55,5))
x_axis = list(np.arange(0,1.1,0.1)) #Importamos la libreria para poder usar un rango de float
plt.plot(x_axis,values,'ko--')  #El tercer argumento especifica color, tipo de punto y tipo de linea
plt.xlim(0,1.0)         #Limite del eje x
plt.ylim(0,50)          #Limite del eje y
plt.title('Practice plot')      #Titulo
plt.xlabel('Horizontal axis')   #Leyenda eje horizontal
plt.ylabel('Vertical axis')     #Leyenda eje vertical
plt.show()
