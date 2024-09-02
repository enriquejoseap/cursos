import numpy as np

# Numpy es una abreviación de Numerical Python. Es un paquete para la computacion científica avanzada y el análisis de datos. Proporciona funcionalidades específicas para manipular datos de tipo array.

# Para hacer uso de las funcionalidades de los arreglos es necesario hacer una instancia antes pasádoles una lista
array = np.array([0, 1, 2, 3, 4, 5])

# A continuación podemos ver la instacia y su tipo
print(array, type(array))

## También es posible hacer una instancia enviando una lista de una variable declarada
notes = [16, 17, 14, 17, 19]

# Tambien se puede indicar el tipo que será el contenido de la lista
ar_notes = np.array(notes, dtype=float)
print(ar_notes, type(ar_notes[0]))

# Array multidimensional (Para agregar más de una dimensión los array deben tener la misma longitud)
matrix = np.array([[1, 2, 3, 4, 5], notes])
print(matrix)

# El atributo ndim se utiliza para conocer la cantidad de dimensiones que contiene un array
print(matrix.ndim) # 2

# El atributo shape se utiliza para conocer la longitud de cada dimension de un array en una tupla: (filas, columnas)
print(matrix.shape) # (2, 5)
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
