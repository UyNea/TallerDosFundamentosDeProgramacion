import pandas as pd
import matplotlib.pyplot as plt

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

DATOS_MAQUINAS = {
    "Máquina 1": [6261, 205, 6801, 4314, 9262, 6165, 9277, 4593, 1764, 1021, 1988, 6044],
    "Máquina 2": [7221, 7173, 5094, 3046, 9015, 1014, 9332, 2368, 2904, 5397, 3178, 8315],
    "Máquina 3": [5709, 6517, 7133, 1593, 3361, 4380, 2928, 916, 6232, 4138, 7420, 1848],
    "Máquina 4": [4486, 5993, 4439, 1242, 8915, 5556, 3573, 7995, 1130, 2718, 2767, 5761],
    "Máquina 5": [1647, 604, 1902, 5101, 9209, 814, 5167, 6224, 261, 6273, 8390, 3492],
    "Máquina 6": [5989, 870, 2198, 9754, 8396, 6389, 6451, 5137, 2051, 7871, 7708, 7600],
    "Máquina 7": [2850, 1904, 2362, 846, 8823, 5989, 108, 9192, 2417, 6382, 2469, 9150],
}


def crear_dataframe():
    tabla = pd.DataFrame(DATOS_MAQUINAS, index=MESES)
    tabla.index.name = "Mes"
    return tabla


def calcular_estadisticas(tabla):
    return tabla.describe()


def calcular_total_por_maquina(tabla):
    return tabla.sum()


def calcular_total_empresa(tabla):
    return tabla.sum().sum()


def grafico_barras_maquina_3(tabla):
    plt.figure()
    plt.bar(tabla.index, tabla["Máquina 3"], label="Máquina 3")
    plt.title("Producción mensual de la Máquina 3")
    plt.xlabel("Mes")
    plt.ylabel("Unidades producidas")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


def grafico_lineas_todas(tabla):
    plt.figure()
    for nombre_maquina in tabla.columns:
        plt.plot(tabla.index, tabla[nombre_maquina], marker="o", label=nombre_maquina)
    plt.title("Producción mensual de las 7 máquinas")
    plt.xlabel("Mes")
    plt.ylabel("Unidades producidas")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


def grafico_barras_total_anual(tabla):
    totales = calcular_total_por_maquina(tabla)
    plt.figure()
    plt.bar(totales.index, totales.values, label="Total anual")
    plt.title("Total anual producido por máquina")
    plt.xlabel("Máquina")
    plt.ylabel("Unidades producidas en el año")
    plt.legend()
    plt.show()
