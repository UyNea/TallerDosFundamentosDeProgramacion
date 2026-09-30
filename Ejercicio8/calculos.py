import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

SUBREGIONES = [
    ["VALLE DE ABURRÁ", "01", 10], ["BAJO CAUCA", "02", 6], ["MAGDALENA MEDIO", "03", 6],
    ["NORDESTE", "04", 10], ["NORTE", "05", 17], ["OCCIDENTE", "06", 19],
    ["ORIENTE", "07", 23], ["SUROESTE", "08", 23], ["URABÁ", "09", 11],
]


def crear_tabla_subregiones():
    return pd.DataFrame(SUBREGIONES, columns=["Nombre", "Código", "Municipios"])


def crear_matriz_temperaturas(n_meses):
    return np.random.randint(15, 31, size=(9, n_meses))


def crear_tabla_paralela(matriz):
    nombres = [fila[0] for fila in SUBREGIONES]
    meses_usados = MESES[:matriz.shape[1]]
    return pd.DataFrame(matriz, index=nombres, columns=meses_usados)


def promedio_por_subregion(matriz):
    lista = []
    for fila in matriz:
        lista.append(sum(fila) / len(fila))
    return lista


def promedio_por_mes(matriz):
    lista = []
    for j in range(matriz.shape[1]):
        suma = 0
        for i in range(matriz.shape[0]):
            suma = suma + matriz[i][j]
        lista.append(suma / matriz.shape[0])
    return lista


def promedio_departamento(matriz):
    return float(matriz.sum()) / matriz.size


def grafico_barras_promedio_subregion(prom_subregion):
    nombres = [fila[0] for fila in SUBREGIONES]
    plt.figure()
    plt.bar(nombres, prom_subregion, label="Promedio de temperatura")
    plt.title("Temperatura promedio por subregión")
    plt.xlabel("Subregión")
    plt.ylabel("Temperatura promedio (°C)")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()


def grafico_lineas_promedio_mes(prom_mes):
    meses_usados = MESES[:len(prom_mes)]
    plt.figure()
    plt.plot(meses_usados, prom_mes, marker="o", label="Promedio del departamento")
    plt.title("Temperatura promedio mensual en Antioquia")
    plt.xlabel("Mes")
    plt.ylabel("Temperatura promedio (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def grafico_barras_municipios():
    nombres = [fila[0] for fila in SUBREGIONES]
    municipios = [fila[2] for fila in SUBREGIONES]
    plt.figure()
    plt.bar(nombres, municipios, label="Municipios")
    plt.title("Número de municipios por subregión")
    plt.xlabel("Subregión")
    plt.ylabel("Número de municipios")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()
