import numpy as np
# Una matriz es un arreglo rectangulas con la siguiente forma:
'''
|A 1,1 . . . A 1,n|
| .    .        . |
| .      .      . |
| .        .    . |
|A m,1 . . . A m,n|
'''
# Dos matrices A y B son multiplicables si el número de columnas de A coincide con el número de filas de B. Las m lineas horizontales se llaman filas, y las n lineas verticales, se llaman columnas

# Matriz transpuesta: Es una matriz la cual los elementos m,n se transforman en una matriz de elementos n,m, es decir, se invierte

# Matriz identidad: Es una matriz cuadrada (m = n) que su diagonal principal contiene 1, y el resto 0

# Producto de matrices las filas de la matriz A se multiplican con cada columna de la matriz B
a = np.array([[5, 2], [4, 8]], float)
b = np.array([[2, 4], [5, 3]], float)
print(a, "\n-----------")
print(b, "\n-----------")

# Aunque se puede utilizar dot() para la multiplicación de matrices no se recomienda pues fue desarrollado específicamente para el producto escalar 
print (np.dot(a, b))

# Para multiplicar matrices correctamente se debe utilizar @
print(a @ b)

# Hay otra alternativa para multiplicar matrices
print(np.matmul(a, b))

# Determinante de una matriz
c = np.array([[8, 5],[3, 4]])
print(c, "\n-----------")
print(np.linalg.det(c), "\n-----------")

# Autovalores y autovectores
vals, vecs = np.linalg.eig(c)
print(vals, "\n-----------")
print(vecs, "\n-----------")