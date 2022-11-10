import numpy as np
import os 
import cv2

def get_radius(circles):
    '''Recibimos un array, el cual tiene en su primer elemento un array de arrays. \n
    El ultimo nivel de arrays tiene [coordenadaX, coordenadaY, radio]'''
    radius = []
    for coords in circles[0,:]:
        radius.append(coords[2])
    return radius

def av_pix(img,circles,size):
    '''Funcion para calcular el brillo de una seccion de una imagen. \n
    Recibimos la imagen, los circulos, y un tamaño del cuadrado que sera usado para el calculo (no tiene que ser muy grande, o abarcara otro objeto). \n '''
    av_value = []
    for coords in circles[0,:]:
        #Tomamos el valor medio de los pixeles en el cuadrado que esta dentro de cada circulo
        col = np.mean(img[coords[1] - size: coords[1] + size, coords[0] - size: coords[0] + size])  
        av_value.append(col)
    return av_value

#Abrimos la imagen con las monedas. El primer parametro es la ubicacion, el segundo el modo de lectura
#Con grayscale, se pasa todo a un único canal de escalas grises
file_name = os.path.join(os.path.dirname(__file__), 'coins.png')
#assert os.path.exists(file_name)                   #Controla que exista la ruta

img = cv2.imread(file_name,cv2.IMREAD_GRAYSCALE)
original_img = cv2.imread(file_name,cv2.IMREAD_UNCHANGED )     #Imagen original sin el cambio de color
img = cv2.GaussianBlur(img, (5,5), 0)                 #Difumina la imagen

#Para ver la imagen
#cv2.imshow('Coin image',img)
#cv2.waitKey(0)                 #Especificamos cuanto se espera para cerrar la imagen. Con 0, espera hasta que se presione una tecla
#cv2.destroyAllWindows() 

#La funcion recibe: la imagen, el metodo usado para encontrar los circulos
#El ratio inverso para el acumulador (se relaciona con el tamaño de la imagen)
#La distancia minima entre los centros de los circulos detectados
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 0.9, 120, param1=50,param2=27,minRadius=60,maxRadius=120)

circles = np.uint16(np.around(circles)) #Redondea los valores del array de circulos
count = 1
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(original_img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(original_img,(i[0],i[1]),2,(0,0,255),3)
    cv2.putText(original_img,str(count), (i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),2)
    count += 1


print(get_radius(circles))
print(av_pix(img,circles,20))

cv2.imshow('detected circles',original_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
