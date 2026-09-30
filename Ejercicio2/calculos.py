import math
import matplotlib.pyplot as plt


def generar_fibonacci(n):
    lista_fib = []
    for i in range(n):
        if i == 0:
            lista_fib.append(0)
        elif i == 1:
            lista_fib.append(1)
        else:
            lista_fib.append(lista_fib[i - 1] + lista_fib[i - 2])
    return lista_fib


def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, int(math.sqrt(numero)) + 1):
        if numero % divisor == 0:
            return False
    return True


def generar_primos(n):
    lista_primos = []
    candidato = 2
    while len(lista_primos) < n:
        if es_primo(candidato):
            lista_primos.append(candidato)
        candidato = candidato + 1
    return lista_primos


def calcular_terminos(x, n):
    fibonacci = generar_fibonacci(n)
    primos = generar_primos(n)
    lista_terminos = []
    for i in range(n):
        valor = (x ** fibonacci[i]) / math.factorial(primos[i])
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
    plt.title("Valor de cada término de la sumatoria")
    plt.xlabel("i (número del término)")
    plt.ylabel("Valor del término")
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
