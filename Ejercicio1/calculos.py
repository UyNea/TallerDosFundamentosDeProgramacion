import math
import matplotlib.pyplot as plt


def termino_sumatoria(x, n, i):
    numerador = math.factorial(x + i)
    denominador = x ** (n - i + 1)
    return numerador / denominador


def calcular_terminos(x, n):
    lista_terminos = []
    for i in range(1, n + 1):
        valor = termino_sumatoria(x, n, i)
        lista_terminos.append(valor)
    return lista_terminos


def calcular_sumas_parciales(lista_terminos):
    lista_parciales = []
    acumulado = 0
    for termino in lista_terminos:
        acumulado = acumulado + termino
        lista_parciales.append(acumulado)
    return lista_parciales


def grafico_lineas_terminos(lista_terminos):
    posiciones = list(range(1, len(lista_terminos) + 1))
    plt.figure()
    plt.plot(posiciones, lista_terminos, marker="o", label="Término i-ésimo")
    plt.yscale("log")
    plt.title("Valor de cada término de la sumatoria")
    plt.xlabel("i (número del término)")
    plt.ylabel("Valor del término (escala log)")
    plt.legend()
    plt.grid(True)
    plt.show()


def grafico_barras_parciales(lista_parciales):
    posiciones = list(range(1, len(lista_parciales) + 1))
    plt.figure()
    plt.bar(posiciones, lista_parciales, label="Suma parcial acumulada")
    plt.title("Suma parcial acumulada de S")
    plt.xlabel("i (número del término)")
    plt.ylabel("Suma parcial acumulada")
    plt.legend()
    plt.show()
