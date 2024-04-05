import random
import time
from memory_profiler import profile

start_time = time.time()
#Comienzo codigo
@profile
def generar_subconjuntos(conjunto):
    subconjuntos = [[]]  # Inicializa con el conjunto vacío
    for elemento in conjunto:
        nuevos_subconjuntos = []
        for subconjunto in subconjuntos:
            nuevo_subconjunto = subconjunto[:]  # Crea una copia del subconjunto actual
            nuevo_subconjunto.append(elemento)  # Agrega el elemento actual al nuevo subconjunto
            nuevos_subconjuntos.append(nuevo_subconjunto)  # Agrega el nuevo subconjunto a la lista de nuevos subconjuntos
        subconjuntos.extend(nuevos_subconjuntos)  # Agrega todos los nuevos subconjuntos a la lista de subconjuntos
    return subconjuntos

# Ejemplo de uso
conjunto = [1, 2, 3]
subconjuntos = generar_subconjuntos(conjunto)
print("Subconjuntos:", subconjuntos)
#fin codigo
end_time = time.time()
elapsed_time = end_time - start_time
print("Tiempo total de ejecución:", elapsed_time, "segundos")
