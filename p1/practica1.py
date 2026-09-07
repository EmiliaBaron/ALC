#Practica 1

import row_echelon as re
import numpy as np

A_a = np.array([
    [1, 1, -2, 1],
    [3, -2, 1, 5],
    [1, -1, 1, 2]
],dtype=float)
A_b = np.array([-2,3,2])
A = np.c_[A_a,A_b]


#chequeo de funcionamiento 
# matrizMultiplicada = A[0] * [[3],[1]]
# print("resultado A[0] * [[3],[1]]\n", matrizMultiplicada)

# print("resultado A[0] * A[1:,0:1]\n", A[0] * A[1:,0:1])
# print("\n")

# res =  A[1:] - A[0] * A[1:,0:1]
# print("resultado A[1:] - A[0] * A[1:,0:1]\n", res)

# res = A[1:] - matrizMultiplicada 
# print("resultado \n", res)

print("matriz asoc y ampl A:\n", A)
print("solucion de sistema A:\n", re.row_echelon(A))
print("\n")



# import numpy as np

# # (a)
# A_a = np.array([
#     [1, 1, -2, 1, -2],
#     [3, -2, 1, 5, 3],
#     [1, -1, 1, 2, 2]
# ], dtype=float)

# (b)
B = np.array([
    [1, 1, 1, -2, 1, 1],
    [1, -3, 1, 1, 1, 0],
    [3, -5, 3, 0, 3, 0]
],dtype=float)

print("matriz asoc y ampl B:\n", B)
print("\n")

# print("resultado B[0] * B[1:,0:1]\n", B[0] * B[1:,0:1])
# print("\n")

# res =  B[1:] - B[0] * B[1:,0:1]
# print("resultado B[1:] - B[0] * B[1:,0:1]\n", res)
# print("\n")

# print("resultado B[1] / B[1,0]\n", res[0] / res[0,1])
# print("\n")

print("solucion de sistema B:\n", re.row_echelon(B))
print("\n")

# (c) (números complejos)
C = np.array([
    [1j, -(1+1j), 0, -1],
    [1, -2, 1, 0],
    [1, 2j, -1, 2j]
], dtype=complex)


print("matriz asoc y ampl C:\n", C)
print("\n")

print("solucion de sistema C:\n", re.row_echelon(C))
print("\n")


# (d) (números complejos)
D = np.array([
    [2, (-1+1j), 0, 1, 2],
    [-1, 3, -3j, 5, 1]
], dtype=complex)

print("matriz asoc y ampl D:\n", D)
print("\n")

print("solucion de sistema D:\n", re.row_echelon(D))
print("\n")

# print("Matriz ampliada (a):\n", A_a)
# print("\nMatriz ampliada (b):\n", A_b)
# print("\nMatriz ampliada (c):\n", A_c)
# print("\nMatriz ampliada (d):\n", A_d)




#rebanar matrices
# A[inicio:fin]
# inicio incluido
# fin excluido
# si no ponés fin, va hasta el final

#A[fila, columna]
# A[1:] → filas desde la 1, todas las columnas
# A[:,1:] → todas las filas, columnas desde la 1
# A[1:,1:] → submatriz sin la primera fila ni la primera columna

#A[1:, 0] - devuelve un vector
#A[1:, 0:1] → devuelve una matriz columna

#Ejercicio3 
print("Ejercicio 3\n")

import numpy as np

# Operaciones básicas
print(1 + 3)
print("\n")

a = 7
b = a + 1
print("b =", b)
print("\n")

# Vectores
v = np.array([1, 2, 3, -1])
w = np.array([2, 3, 0, 5])

print("v + w =", v + w)
print("2 * v =", 2 * v)
print("v ** 2 =", v ** 2)
print("\n")

# Matrices
# (ejecutar los comandos uno a uno para ver los resultados)
A = np.array([
    [1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4],
    [2, 3, 4, 5, 6],
    [0, 0, 1, 2, 3],
    [0, 0, 0, 0, 1]
])

print("Matriz A: \n", A)
print("\n")

# Submatrices
print("Matriz A[0:2, 3:5]:")
print(A[0:2, 3:5])
print("\nMatriz A[:2, 3:]:")
print(A[:2, 3:])
print("\n")

# Selección de filas específicas
print("Matriz A[[0, 2, 4], :]:")
print(A[[0, 2, 4], :])
print("\n")

# Índices
ind = np.array([0, 2, 4])
print("ind: ", ind)
print("\n")


# Elementos en posiciones (0,0), (2,2), (4,4)
print("Matriz A[ind, ind]:")
print(A[ind, ind])
print("\n")


# Selección tipo submatriz usando broadcasting
print("Matriz A[ind, ind[:, None]]:")
# ind[:, None] convierte el ind en una columna
# ind[:, None] = 
# [[0],
#  [2],
#  [4]]
#broadcasting copia el array hasta que encaja
#ind = [0, 2, 4]
#ind[:, None] = 
# [[0],
#  [2],
#  [4]]

#resultados:
# ind = [[0 2 4]
#  [0 2 4]
#  [0 2 4]]

# y

# ind[:, None] = 
# [[0 0 0]
#  [2 2 2]
#  [4 4 4]]

print("""se generan todas las combinaciones de índices
(invertido columna-fila)
(0,0) (0,2) (0,4)
(2,0) (2,2) (2,4)
(4,0) (4,2) (4,4)""")

print("\n")
print("Matriz A[ind, ind]:")
print(A[ind, ind[:, None]])
print("\n")

# Números complejos
print(1j * 1j)
print((1 + 2j) * 1j)


