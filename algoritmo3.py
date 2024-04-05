import random
import time
from memory_profiler import profile

@profile
def operacion_intensiva_memoria(n):  # O(1)
    """Operación que genera un gran uso de memoria temporalmente."""
    gran_lista = [random.random() for _ in range(n)] # O(n)
    time.sleep(1)  # Simulamos un procesamiento
    return sum(gran_lista) # O(1)

@profile
def operacion_intensiva_cpu(n): # O(1)
    """Operación que consume tiempo de CPU."""
    contador = 0
    for _ in range(n): # O(n)
        contador += random.random() 
        time.sleep(0.01)  # Añade un pequeño retardo para simular procesamiento

def main():
    n = 500000
    for i in range(5): # O(n^3)
        print(f"Pico {i+1}: Operación intensiva en memoria")
        operacion_intensiva_memoria(n)
        print(f"Pico {i+1}: Operación intensiva en CPU")
        operacion_intensiva_cpu(100)

if __name__ == "__main__":
    main()
