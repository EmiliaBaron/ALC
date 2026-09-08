import numpy as np

#a 
print( "Item a\n")
p = 1e34
print(f" representacion            1e34: {format(1e34, '.20f')}") 
print(f" representacion        1e34 + 1: {format(1e34 + 1, '.20f')}")
print(f" representacion 1e34 + 1 - 1e34: {format(1e34 + 1 - 1e34, '.20f')}")
q = 1 
print(p + q - p)
#Da lo mismo porque la representación el valor que realmente se guarda en float de 
# 1e34 es igual al valor que se guarda en float de 1e34 + 1. 
# dos números muy distintos en magnitud hace que el más chico sea ignorado

#PREGUNTA: tiene que ver el epsilon con esto? Esta explicación basta?

# b
print( "Item b\n")
p = 100
q = 1e-15
print(f" representacion         1e-15: {format(1e-15, '.20f')}") 
print(f" representacion       epsilon: {format(np.finfo(float).eps, '.20f')}") 
print(f" representacion   100 + 1e-15: {format(100 + 1e-15, '.20f')}") 

print(f"(p+q)+ q = {(p+q)+ q} ") 
print(f"((p + q) + q) + q = {((p + q) + q) + q}" )
print( q > np.finfo(float).eps)

print(f"p + 2q = {p + 2*q} ") 
print(f"p + 3q = {p + 3*q} ")
#por que no calcula bien si q es mayor a epsilon?
# dos números muy distintos en magnitud hace que el más chico sea ignorado

#c)
print( "Item c\n")
print(f"| 0.1+0.2 = 0.3 -> {(0.1+0.2) == 0.3}")
print(f"| 0.1+0.2 = {format(0.1+0.2, '.20f')}")
print(f"|     0.1 = {format(0.1, '.20f')}")
print(f"|     0.2 = {format(0.2, '.20f')}")

print(f"|     0.3 = {format(0.3, '.20f')}")

#el problema es que no existe mantisa de finitos bits para representar 0.3 ni 0.1 ni 0.2
# hasta que punto tengo que entender qué es lo que pasa en bajo nivel?

#d)
print( "Item d\n")
print(f"| 0.1+0.3 == 0.4 -> { 0.1+0.3 == 0.4}")
print(f"| 0.1+0.3 = {format(0.1+0.3, '.20f')}")
print(f"|     0.4 = {format(0.4, '.20f')}")

#NO PUEDO ENTENDER PORQUE C DA MAL PERO D DA BIEN

#e)
print("\n")
print( "Item e")
print(f"|1e-323 ={format(1e-323, '.24f' )}")
print(f" {np.finfo(float).tiny} > 1e-323 = {np.finfo(float).tiny > 1e-323} ")

#esto ocurre porque 1e-23 es más chico que el mínimo numero que se puede representar en float

#f)
print("\n")
print( "Item f")
print(f"|1e-324 ={format(1e-324, '.24f' )}")
print(f" {np.finfo(float).tiny} > 1e-324 = {np.finfo(float).tiny > 1e-324} ")

#esto ocurre porque 1e-23 y 1e-24 es más chico que el mínimo numero que se puede representar en float

#g) 
print("\n")
print( "Item g")
#si yo pongo float -> equivale a doble (float 64)?
print(f"| epsilon = {format(np.finfo(float).eps, '.20f' )}")
print(f"| epsilon/2 = {format(np.finfo(float).eps/2, '.20f' )}")

#h) 
print("\n")
print( "Item h")
print(f"| 1 + epsilon/2 = {format(1 + np.finfo(float).eps/2, '.20f' )}")
print(f"| (1 + epsilon/2) epsilon/2 = {format((1 + np.finfo(float).eps/2) + np.finfo(float).eps/2, '.20f' )}")
# esto ocurre porque el epsilon de máquina es el número más chico tal que 1 + eps != 1

#i)
print("\n")
print( "Item i")
print(f"| 1 + (epsilon/2 + epsilon/2)  = {format(1 + (np.finfo(float).eps/2 + np.finfo(float).eps/2), '.20f' )}")
# cuando se suman los eps/2 por separado forman eps, entonces hacer 1 + eps si genera un cambio

#j)
print("\n")
print( "Item j")
print(f"| ((1 + epsilon/2) + epsilon/2) -1   = {format(((1 + np.finfo(float).eps/2) + np.finfo(float).eps/2) -1 , '.20f' )}")
# los epsilons son muy chicos para producir un cambio guardable en 1 entonces al final queda 1 -1 = 0 

#k)
print("\n")
print( "Item k")
print(f"| epsilon = {format(np.finfo(float).eps, '.20f' )}")
print(f"| 1 + (epsilon/2 + epsilon/2) - 1   = {format(1 + (np.finfo(float).eps/2 + np.finfo(float).eps/2) -1 , '.20f' )}")
# como primero se suman las mitades de eps, se termina haciendo 1 + eps que si genera cambio guardable por lo que al restar 1 es igual a eps

#l)
print("\n")
print( "Item l")

for j in range(1,25):
    s =  np.sin((10**j) * np.pi)
    print(f"| sin(π10^{j}) = {s}")

# sen(10π) = 0.521246
# sen(10^2 π) = -0.71

import matplotlib.pyplot as plt

x = np.linspace(1,25, 50)

f = lambda t: np.sin((10**t) * np.pi)
#g = lambda t: 2*(t**2)/(np.sqrt(2*(t**2)+1)+1)

plt.plot(x, f(x), label='f(x)')
#plt.plot(x, g(x), label='g(x)')
plt.legend()
plt.show()

#el gráfico es mucho más feo que el de geogebra y no entiendo por que 

#m)
print("\n")
print( "Item m")

for j in range(1,25):
    s =  np.sin(np.pi/2 + (10**j) * np.pi)
    print(f"| sin(π/2 + π10^{j}) = {s}")

# sen(10π) = 0.521246
# sen(10^2 π) = -0.71

import matplotlib.pyplot as plt

x = np.linspace(1,25, 50)

f = lambda t: np.sin((10**t) * np.pi)
g = lambda t: np.sin(np.pi/2 + (10**t) * np.pi)

plt.plot(x, f(x), label='f(x)')
plt.plot(x, g(x), label='g(x)')
plt.legend()
plt.show()

#el gráfico es mucho más feo que el de geogebra y no entiendo por que 
#gráfico de geogebra: dos funciones que oscilan muchas veces por milimetro
#aparte parece que el gráfico es distinto a los cálculos