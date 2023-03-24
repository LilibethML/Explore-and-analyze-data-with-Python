#  Numpy nos provee de herramientas matematicas para poder hacer analisis
# numerico. Abajo un ejemplo:
import numpy as np

data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
grades = np.array(data)
print(grades)

# los arrays se comportan como  vectores. Si multiplicamos la lista *2 y 
# el array tambien, vemos que la lista se imrpime dos veces, y usando 
# array sí nos devuelve una lista del mismo tamaño con los valores 
#multiplicados por dos. 

print (type(data),'x 2:', data * 2)
print('---')
print (type(grades),'x 2:', grades * 2)

# ndarray significa arreglo de n dimensiones. En este caso, nuestro array es
# de una dim. 

print(grades.shape) # nos dice la dimension del arreglo y sus elementos
print(grades[0]) # nos da el valor en la posicion del index
print(grades.mean()) #nos da el promedio del array 
