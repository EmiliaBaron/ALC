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
print(f"| 0.1+0.3 == 0.4 -> { 0.1+0.3 == 0.4}")
print(f"| 0.1+0.3 = {format(0.1+0.3, '.20f')}")
print(f"|     0.4 = {format(0.4, '.20f')}")


