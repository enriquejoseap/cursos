import numpy as np

# los array nos permiten realizar operaciones aritméticas elemento a elemento directamente

array1 = np.arange(1, 9)
print(array1)

# Podemos utilizar el atributo shape para transformar el array en un arreglo multidimensional
array1.shape = (2, 4)
print(array1)

# Suma de arrays. Los arreglos deben ser de la misma dimensión
print("Suma\n", array1 + array1)

# Resta de arrays. Los arreglos deben ser de la misma dimensión
print("Resta\n", array1 - array1)

# Multiplicación de arrays. La multiplicación no será asociativa
print(
    "Multiplicación\n",
    np.array([[2, 0, 1], [3, 0, 0], [5, 1, 1]])
    * np.array([[1, 0, 1], [1, 2, 1], [1, 1, 0]]),
)

# División de arreglos. La división no será asociativa
print("División\n", array1 / array1)

# Potenciación de arreglos.
print("Potenciación\n", array1 ** array1)

# División de arreglos. La división entera no será asociativa
print("División entera\n", array1 // array1)