from memory_profiler import profile


@profile
def imprimir(lista):
    n = lista
    print(lista)


if "__main__" == __name__:
  lista = 2
  imprimir(lista)
