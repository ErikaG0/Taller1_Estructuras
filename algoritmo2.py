from memory_profiler import profile

@profile
def mi_algoritmo(n): # O(1)
    lista = list(range(n)) # o(1)
    pares = []  # O(1)
    for i in lista: 
        for j in lista:  # O(n^2)
            pares.append((i, j))
    return pares

if __name__ == "__main__":
    mi_algoritmo(1000)   # O(1)
