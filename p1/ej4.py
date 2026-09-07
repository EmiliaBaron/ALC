import numpy as np
import matplotlib.pyplot as plt  # libreria para graficar
import row_echelon as re

# ...
# Aca, crear la matriz y resolver el sistema para calcular a, b y c.

A = np.array([
    [1, 1, 1, 1],
    [4, 2, 1, 2],
    [9, 3, 1, 0]    
])

print("matriz A:\n", A)
print("\n")
print("solucion de sistema A:\n", re.row_echelon(A))
print("\n")

a = -3/2
b = 11/2
c = -3

# ...



xx = np.array([1, 2, 3])
yy = np.array([1, 2, 0])

x = np.linspace(0, 4, 100)  # genera 100 puntos equiespaciados entre 0 y 4.

f = lambda t: a*t**2 + b*t + c  # esto genera una funcion f de t.

plt.plot(xx, yy, '*')
plt.plot(x, f(x))
plt.show()
