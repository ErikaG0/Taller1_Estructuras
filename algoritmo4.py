import random
import time
from memory_profiler import profile

@profile
def busqueda(arr, elemento_buscado): 
    izquierda, derecha = 0, len(arr) - 1 #O(1)
    while izquierda <= derecha: #O(n)
        medio = (izquierda + derecha) // 2 #O(log n)
        medio_valor = arr[medio]
        
        if medio_valor == elemento_buscado: #O(1)
            return medio
        elif elemento_buscado < medio_valor:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return -1

indice = busqueda([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)#O(1)
