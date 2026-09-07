import numpy as np

#A.shape[0] -> devuelve la cantidad de filas de A
#A.shape[1] -> devuelve la cantidad de columnas de A

#(a) Calcular la traza de una matriz

def traza(A):
    r, c = A.shape

    traza = 0

    if r != c :
        return "la traza es solo para matrices cuadradas"
    
    for i in range(r):
        traza = traza + A[i][i]

    return traza

# A = np.array([
#     [1, 2, 3, 4, 5],
#     [0, 1, 2, 3, 4],
#     [2, 3, 4, 5, 6],
#     [0, 0, 1, 2, 3],
#     [0, 0, 0, 0, 1]
# ])

# print("Matriz A:\n", A)
# print("tr(A): ", traza(A))

# B = np.array([
#     [1j, 0, 2 + 1j],
#     [-1, 1 - 1j, 0],
#     [2, 0, -1]
# ], dtype=complex)

# print("Matriz B:\n", B)
# print("tr(B): ", traza(B))


#(b) Calcular la sumatoria de todos los elementos de una matriz.

def sumatoriaElementos(A):
    r, c = A.shape

    sumatoria = 0

    for i in range(r):
        for j in range(c):
            sumatoria = sumatoria + A[i][j]

    return sumatoria

# A = np.array([
#     [1, 0, 0, 2],
#     [0, -2, 3, -1],
#     [-1, 0, 1, 4],
#     [0, 1, -2, 0]
# ])

# print("Matriz A:\n", A)
# print("sumatoria de elementos de A: ", sumatoriaElementos(A))

#(c) Determinar si la sumatoria de elementos positivos es mayor que la sumatoria (en m´odulo) de
#los elementos negativos de una matriz.

def determinarSumPositivoMayorASumNegativos(A):
    r, c = A.shape

    sumatoriaPositivos = 0
    sumatoriaNegativos = 0

    for i in range(r):
        for j in range(c):

            if (A[i][j] >=0):
                sumatoriaPositivos = sumatoriaPositivos + A[i][j]

            else: 
                sumatoriaNegativos = sumatoriaNegativos + abs(A[i][j])


    return sumatoriaPositivos > sumatoriaNegativos

A = np.array([
    [1, 0, 0, 2],
    [0, -2, 3, -1],
    [-1, 0, 1, 4],
    [0, 1, -2, 0]
])

print("Matriz A:\n", A)
print("sumatoria de positivos de A es mayor a su sumatoria en módulo de sus negativos: ", determinarSumPositivoMayorASumNegativos(A))