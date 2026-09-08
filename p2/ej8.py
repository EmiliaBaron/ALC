import numpy as np

# Hago un doble for para calcular las sumas parciales de 1/n hasta distintos valores
for n in range(200,1001,200):
    s =  np.float16(0)
    for i in range(1,n):
        s += np.float16(1/i)
    print(f'Suma de los primeros {n} terminos de 1/n : {s}')
f'Conclusión: la serie armonica converge a {s} :('

# si se pone float en vez de np.float16 funciona de lo más bien

#¿Qu´e deber´ıa ocurrir para que el resultado num´erico sea Inf? 
#no se me ocurre que debería ocurrir para que el resultado sea inf
# porque sumando numeros concretos nunca va a dar infinito. Por ahí algo con límites?

#  ¿Cu´al es la mejor estrategia para realizar num´ericamente una
# sumatoria de t´erminos positivos?

# supongo que sumando de a bloques, primero se suman los 1/j del 1 al 100, luego
# se suman los 1/j del 100 a 200 como segundo bloque y por último se suman los bloques,
# así evitamos la suma sin efecto por la diferencia de magnitud 