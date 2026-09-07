import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import numpy.linalg as lng
import numpy as np
import pandas as pd

#no estudiar que hace las funciones de plot 

def pointsGrid(esquinas):
    # crear 10 lineas horizontales
    [w1, z1] = np.meshgrid(np.linspace(esquinas[0,0], esquinas[1,0], 46),
                        np.linspace(esquinas[0,1], esquinas[1,1], 10))

    [w2, z2] = np.meshgrid(np.linspace(esquinas[0,0], esquinas[1,0], 10),
                        np.linspace(esquinas[0,1], esquinas[1,1], 46))

    w = np.concatenate((w1.reshape(1,-1),w2.reshape(1,-1)),1)
    z = np.concatenate((z1.reshape(1,-1),z2.reshape(1,-1)),1)
    wz = np.concatenate((w,z))
                         
    return wz

def calcularAx(A,x): #si A es de mxn, x tiene que ser de largo m y devuelve vector de largo n
    #falla si no se cumplen las dimensiones

    f,c = A.shape
    R = [0] * f  # MUCHO MÁS RÁPIDO QUE np.zeros(f)

    for i in range(f):
        for j in range(c):
            R[i] += A[i][j] * x[j]

    return R

def proyectarPts(T, wz):
    assert(T.shape == (2,2)) # chequeo de matriz 2x2
    assert(T.shape[1] == wz.shape[0]) # multiplicacion matricial valida   

    xy = calcularAx(T,wz)
    

    return xy

## rotar y que se yo
def producto_matriz(A,B): #falla si no se cumplen las dimensiones

    fa, ca = A.shape
    fb, cb = B.shape

    if (ca != fb):
        raise(ValueError("columnas de A debe ser igual a filas de b"))

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

    return producto_matriz(escala(s), rota(theta))
          
def vistform(T, wz, titulo=''):
    # transformar los puntos de entrada usando T
    xy = proyectarPts(T, wz)
    if xy is None:
        print('No fue implementada correctamente la proyeccion de coordenadas')
        return
    # calcular los limites para ambos plots
    minlim = np.min(np.concatenate((wz, xy), 1), axis=1)
    maxlim = np.max(np.concatenate((wz, xy), 1), axis=1)

    bump = [np.max(((maxlim[0] - minlim[0]) * 0.05, 0.1)),
            np.max(((maxlim[1] - minlim[1]) * 0.05, 0.1))]
    limits = [[minlim[0]-bump[0], maxlim[0]+bump[0]],
               [minlim[1]-bump[1], maxlim[1]+bump[1]]]             

    fig, (ax1, ax2) = plt.subplots(1, 2)         
    fig.suptitle(titulo)
    grid_plot(ax1, wz, limits, 'w', 'z')    
    grid_plot(ax2, xy, limits, 'x', 'y')    
    
def grid_plot(ax, ab, limits, a_label, b_label):
    ab = np.array(ab)
    ax.plot(ab[0,:], ab[1,:], '.')
    ax.set(aspect='equal',
           xlim=limits[0], ylim=limits[1],
           xlabel=a_label, ylabel=b_label)


def main():
    print('Ejecutar el programa')
    # generar el tipo de transformacion dando valores a la matriz T
    T = pd.read_csv('T.csv', header=None).values

    print(T)

    corners = np.array([[0,0],[100,100]])
    # corners = np.array([[-100,-100],[100,100]]) array con valores positivos y negativos
    wz = pointsGrid(corners)
  
    #vistform(T, wz, 'Deformar coordenadas')

    f = np.array([[0.5,0],[0, 0.5]])
   # vistform(f, wz, "encojer coordenadas")
    #vistform(lng.inv(f), wz, "agrandar coordenadas")



    #Ejercicio 3 
    a = 1
    b = 0  #mientras lo pasás a 1 se va a torciendo tipo "desformar coordenadas"
    c = 0
    d = 1
    f3 = np.array([[a,b],[c,d]])
    vistform(f3, wz, "Ejercicio 3b")

    #c
    a = 1
    b = 0  
    c = 0
    d = 1
    f3 = np.array([[a,b],[c,d]])
    vistform(f3, wz, "Ejercicio 3b")


    #ejercicio 5
    f5 = rota_y_escala(np.pi/4, [2,3])
    vistform(f5, wz, "ejercicio 5")

    plt.show()

    
if __name__ == "__main__":
    main()
