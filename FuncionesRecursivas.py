import math
from time import time
#Variables globales aplha y beta
a = 6
b = 5

def f(n) -> int:
    """Función recursiva que implementa
    f(n)=f(n-5)+f(n-10)+f(n-15)+f(n-20)+f(n-25)+f(n-30)

    Args:
        n (n): Valor al que se le calculará la función.

    Returns:
        int: Valor resultante de aplicar la función.
    """
    assert 0 <= n, "El número debe ser positivo."
    if 0 <= n and n < a*b:
        return n
    return f(n-b*1) + f(n-b*2) + f(n-b*3) + f(n-b*4) + f(n-b*5) + f(n-b*6)

def f_cola(n) -> int:
    """Función recursiva que implementa
    f(n)=f(n-5)+f(n-10)+f(n-15)+f(n-20)+f(n-25)+f(n-30)
    de manera recursiva de cola.

    Args:
        n (n): Valor al que se le calculará la función.

    Returns:
        int: Valor resultante de aplicar la función.
    """
    assert 0 <= n, "El número debe ser positivo."
    f1 = n%b
    def f_cola_aux(n1, n2, n3, n4, n5, n6, i) -> int: #definición de la función auxiliar
        if i == (n-(f1+b*5))//b: #Se itera el mismo número de veces, que altura del árbol de recursión
            return n1
        return f_cola_aux(n1+n2+n3+n4+n5+n6, n1, n2, n3, n4, n5, i+1)
    if n < a*b: #Caso base
        return n
    return f_cola_aux(f1+b*5, f1+b*4, f1+b*3, f1+b*2, f1+b, f1, 0)

def f_iterativo(n) -> int:
    """Función recursiva que implementa
    f(n)=f(n-5)+f(n-10)+f(n-15)+f(n-20)+f(n-25)+f(n-30)
    de manera iterativa.

    Args:
        n (n): Valor al que se le calculará la función.

    Returns:
        int: Valor resultante de aplicar la función.
    """
    assert 0 <= n, "El número debe ser positivo."
    if n < a*b: #Caso base
        return n
    f1 = n%b
    f2 = f1+b
    f3 = f1+b*2
    f4 = f1+b*3
    f5 = f1+b*4
    f6 = f1+b*5
    iteraciones = (n-(f1+b*5))//b
    t = 0
    i = 0
    while i != iteraciones: #Mientras aun no se han hecho todas las iteraciones
        t = f6 + f5 + f4 + f3 + f2 + f1
        f1 = f2
        f2 = f3
        f3 = f4
        f4 = f5
        f5 = f6
        f6 = t
        i += 1
    return t

def prueba(f, n):
    max = 0
    min = math.inf
    prom = 0
    for i in range(0,300):
        tiempo_i = time()
        f(n)
        tiempo_f = time() - tiempo_i
        if tiempo_f < min:
            min = tiempo_f
        elif tiempo_f > max:
            max = tiempo_f
        prom += tiempo_f
    prom /=300
    print(max, prom, min)

for i in range(40, 180, 20):
    print("Prueba con n = " + str(i))
    prueba(f, i)
    prueba(f_cola, i)
    prueba(f_iterativo, i)
    print("")