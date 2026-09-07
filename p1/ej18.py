import numpy as np

A = np.array([
    [1, 0, 0, 2],
    [0, -2, 3, -1],
    [-1, 0, 1, 4],
    [0, 1, -2, 0]
])

print("Matriz A:\n", A)
print("det(A): \n", np.linalg.det(A))

B = np.array([
    [1j, 0, 2 + 1j],
    [-1, 1 - 1j, 0],
    [2, 0, -1]
], dtype=complex)

print("Matriz B:\n", B)
print("det(B): \n", np.linalg.det(B))
