import numpy as np

a = np.array([1, 2, 3], float)
b = np.array([0, 1, 1], float)

# Para realizar un producto escalar se utiliza el metodo dot()
print(np.dot(a, b))

# También podemos realizar el mismo producto escalar utilizando el método directamente en la variable
print(a.dot(b))



