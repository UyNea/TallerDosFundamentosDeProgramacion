import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def crear_matriz(n):
    return np.random.randint(10, 100, size=(n, n))


def extraer_diagonal_principal(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(int(matriz[i][i]))
    return diagonal


def extraer_diagonal_secundaria(matriz):
    n = len(matriz)
    diagonal = []
    for i in range(n):
        diagonal.append(int(matriz[i][n - 1 - i]))
    return diagonal


def calcular_estadisticas(matriz):
    return pd.DataFrame(matriz).describe()


def grafico_puntos(diag_principal, diag_secundaria):
    plt.figure()
    plt.scatter(diag_principal, diag_secundaria, label="(principal, secundaria)")
    plt.title("Diagonal principal vs diagonal secundaria")
    plt.xlabel("Diagonal principal")
    plt.ylabel("Diagonal secundaria")
    plt.legend()
    plt.grid(True)
    plt.show()


def grafico_lineas(diag_principal, diag_secundaria):
    posiciones = list(range(len(diag_principal)))
    plt.figure()
    plt.plot(posiciones, diag_principal, marker="o", label="Diagonal principal")
    plt.plot(posiciones, diag_secundaria, marker="s", label="Diagonal secundaria")
    plt.title("Valores de las diagonales por posición")
    plt.xlabel("Posición dentro de la diagonal")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(True)
    plt.show()
