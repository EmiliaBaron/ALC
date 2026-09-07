import numpy as np

#entorno source labo2/bin/activate
#correr tests -> python -m pytest tests02.py

def producto_matriz(A,B): #falla si no se cumplen las dimensiones

    fa, ca = A.shape
    fb, cb = B.shape

    R = np.zeros((fa,cb))

    for i in range(fa):
        for j in range(cb):
            for c in range(ca): #o fb
                R[i][j] += A[i][c] * B[c][j]

    return R


def rota(theta):  #pasa
    """
    Recibe un angulo theta y retorna una matriz de 2x2 que rota un vector dado en un angulo theta
    """

    return np.array([[np.cos(theta), - np.sin(theta)],[np.sin(theta), np.cos(theta)]]) 


def escala(s): #pasa
    """
    % Recibe una tira de números s y retorna una matriz cuadrada de n x n, donde n es el tamano de s.
    La matriz escala la componente i de un vector de Rn en un factor s[i]
    """
    n = len(s)
    M = np.zeros((n,n))

    for i in range(n):

        M[i][i] = s[i]

    return M


def rota_y_escala(theta,s): #PASAA
    """
    % Recibe un ángulo theta y una tira de números s, y retorna una matriz de 2 x 2 que rota el vector en 
    un ángulo theta y luego lo escala en un factor s
    """

    return escala(s)@rota(theta)


def afin(theta,s,b): #PASA
    """
    % Recibe un ángulo theta, una tira de números s (en R2), y un vector b en (R2) y 
    retorna una matriz de 3 x 3 que rota el vector en un ángulo theta, luego lo escala en un factor s y por último lo muevo en un valor fijo b
    """

    M = rota_y_escala(theta, s)

    R = np.zeros((3,3))

    fm, cm = M.shape

    for i in range(fm):
        for j in range(cm):
            R[i][j] = M[i][j]

    R[0][2] = b[0]
    R[1][2] = b[1]
    R[2][2] = 1

    return R



    return R

def trans_afin(v,theta,s,b): #pasa
    """
    % Recibe un vector v (en R2), un ángulo theta, una tira de números s (en R2), 
    y un vector b en (R2) y retorna el vector w resultante de aplicar la transformacion afin a v
    """
    v3 = np.zeros((3))
    v3[0] = v[0]
    v3[1] = v[1]
    v3[2] = 1

    res = afin(theta,s,b)@v3

    return np.array(res[:-1])
    


def calcularAx(A,x): #si A es de mxn, x tiene que ser de largo m y devuelve vector de largo n
    #falla si no se cumplen las dimensiones

    f,c = A.shape
    R = [0] * f  # MUCHO MÁS RÁPIDO QUE np.zeros(f)

    for i in range(f):
        for j in range(c):
            R[i] += A[i][j] * x[j]
            
if __name__ == "__main__":

    A = np.array([[2, 3, -1], [5, 4, 2]])
    B = np.array([[4,3],[5, 4],[-1,2]])

    print(producto_matriz(A,B))
