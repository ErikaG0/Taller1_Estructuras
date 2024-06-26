import random
import time
from memory_profiler import profile

def generar_subconjuntos(conjunto):
    subconjuntos = [[]]  # Inicializa con el conjunto vacío
    for elemento in conjunto: 
        nuevos_subconjuntos = []
        for subconjunto in subconjuntos: # O(2^n)
            nuevo_subconjunto = subconjunto[:]  # Crea una copia del subconjunto actual
            nuevo_subconjunto.append(elemento)  # Agrega el elemento actual al nuevo subconjunto
            nuevos_subconjuntos.append(nuevo_subconjunto)  # Agrega el nuevo subconjunto a la lista de nuevos subconjuntos
        subconjuntos.extend(nuevos_subconjuntos)  # Agrega todos los nuevos subconjuntos a la lista de subconjuntos
    return subconjuntos

# Ejemplo de uso
conjunto = [1, 2, 3]
subconjuntos = generar_subconjuntos(conjunto)
print("Subconjuntos:", subconjuntos)



