import math
import random

nombre_archivo = "notas.txt"


def numeros_aleatorios(cantidad):
    lista = []
    for i in range(0, cantidad):
        lista.append(random.randint(0, 20))
    return lista


def crear_archivo():
    cantidad_notas = int(input("Ingresa el total de notas:"))
    notas_aleatorias = numeros_aleatorios(cantidad_notas)

    archivo = open(nombre_archivo, "w+")
    for nota in notas_aleatorias:
        archivo.write("{}\n".format(nota))

    archivo.close()


def obtener_cuadrados():
    archivo = open(nombre_archivo, "w+")
    notas = archivo.read().split("\n")
    for nota in notas:
        if len(nota) > 0:
            cuadrado = math.sqrt(int(nota))

    archivo.close()


crear_archivo()
