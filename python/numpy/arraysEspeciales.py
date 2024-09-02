import numpy as np

# Arrays Especiales
'''
- zeros(): Produce un ndarray con todos sus elementos igual a cero
- ones(): Produce un ndarray con todos sus elementos igual a uno
- indentity(): Produce una matriz cuadrada identidad
- arange(): Produce un nuevo ndarray cuyos elementos están en el rango especificado
'''
# Enviamos [num filas, num columnas] en tupla o lista
array1 = np.zeros((1, 2), dtype=float)
print(array1)

# Enviamos [num filas, num columnas] en tupla o lista
array2 = np.ones((3, 4), dtype=float)
print(array2)

# Enviamos la dimension de la matriz
array3 = np.identity((4), dtype=float)
print(array3)

# Enviamos el rango que queremos recibir
array4 = np.arange(1, 9)
print(array4)
