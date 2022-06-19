import random


def numeros_aleatorios():
    lista = []
    for i in range(0, 10):
        lista.append(random.randint(0, 20))
    return lista


def numeros_no_repetidos(aleatorios):
    no_repetidos = []
    for numero in aleatorios:
        if aleatorios.count(numero) == 1:
            no_repetidos.append(numero)
    return no_repetidos


def orden_menor_a_mayor(lista):
    return sorted(lista)


def orden_mayor_a_menor(lista):
    return sorted(lista, reverse=True)


def encontrar_mayor(lista):
    return max(lista)


# 1 Genero lista de 10 numeros aleatorios
lista_aleatorios = numeros_aleatorios()
print("Lista de 10 numeros aleatorios:", lista_aleatorios)

# 2 Numeros aleatorios no repetidos
lista_no_repetidos = numeros_no_repetidos(lista_aleatorios)
print("Lista de numeros aleatorios no repetidos:", lista_no_repetidos)

# 3.1 Lista de mayor a menor (no repetidos) (asc)
lista_menor_a_mayor = orden_menor_a_mayor(lista_no_repetidos)
print("Lista de numeros no repetidos de Menor a Mayor:", lista_menor_a_mayor)

# 3.2 Lista de mayor a menor (no repetidos) (desc)
lista_mayor_a_menor = orden_mayor_a_menor(lista_no_repetidos)
print("Lista de numeros no repetidos de Mayor a Menor:", lista_mayor_a_menor)

# 4 Maximo valor de la lista
mayor = encontrar_mayor(lista_no_repetidos)
print("El mayor valor no repetido es", mayor)
