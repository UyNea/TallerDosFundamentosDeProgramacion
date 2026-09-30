import numpy as np
import matplotlib.pyplot as plt


def crear_matriz(n, m):
    return np.random.randint(0, 101, size=(n, m))


def promedios_por_fila(matriz):
    lista_promedios = []
    for fila in matriz:
        lista_promedios.append(sum(fila) / len(fila))
    return lista_promedios


def promedios_por_columna(matriz):
    n_filas = len(matriz)
    n_columnas = len(matriz[0])
    lista_promedios = []
    for j in range(n_columnas):
        suma = 0
        for i in range(n_filas):
            suma = suma + matriz[i][j]
        lista_promedios.append(suma / n_filas)
    return lista_promedios


def estadisticas_globales(matriz):
    n_filas = len(matriz)
    n_columnas = len(matriz[0])
    maximo = matriz[0][0]
    fila_max, col_max = 0, 0
    minimo = matriz[0][0]
    fila_min, col_min = 0, 0
    suma = 0
    for i in range(n_filas):
        for j in range(n_columnas):
            dato = matriz[i][j]
            suma = suma + dato
            if dato > maximo:
                maximo = dato
                fila_max, col_max = i, j
            if dato < minimo:
                minimo = dato
                fila_min, col_min = i, j
    resultado = {
        "promedio": suma / (n_filas * n_columnas),
        "maximo": int(maximo), "fila_max": fila_max, "col_max": col_max,
        "minimo": int(minimo), "fila_min": fila_min, "col_min": col_min,
    }
    return resultado


def grafico_barras_filas(prom_filas):
    numeros = list(range(1, len(prom_filas) + 1))
    plt.figure()
    plt.bar(numeros, prom_filas, label="Promedio por fila")
    plt.title("Promedio de cada fila")
    plt.xlabel("Número de fila")
    plt.ylabel("Promedio")
    plt.legend()
    plt.show()


def grafico_barras_columnas(prom_columnas):
    numeros = list(range(1, len(prom_columnas) + 1))
    plt.figure()
    plt.bar(numeros, prom_columnas, label="Promedio por columna")
    plt.title("Promedio de cada columna")
    plt.xlabel("Número de columna")
    plt.ylabel("Promedio")
    plt.legend()
    plt.show()


def grafico_mapa_calor(matriz):
    plt.figure()
    plt.imshow(matriz)
    plt.colorbar(label="Valor")
    plt.title("Mapa de calor de la matriz")
    plt.xlabel("Columna")
    plt.ylabel("Fila")
    plt.show()
