import matplotlib.pyplot as plt

RANGO_MINIMO = 5400
RANGO_MAXIMO = 6200000

TABLA_COLORES = {
    0: "NEGRO", 1: "MARRÓN", 2: "ROJO", 3: "NARANJA", 4: "AMARILLO",
    5: "VERDE", 6: "AZUL", 7: "VIOLETA", 8: "GRIS", 9: "BLANCO",
}


def calcular_valor_ohmios(banda1, banda2, banda3):
    return (banda1 * 10 + banda2) * 10 ** banda3


def formatear_ohmios(valor):
    if valor >= 1000000:
        return str(valor / 1000000) + " MΩ"
    elif valor >= 1000:
        return str(valor / 1000) + " kΩ"
    else:
        return str(valor) + " Ω"


def buscar_mayor_menor(lista_resistencias):
    mayor = lista_resistencias[0]
    menor = lista_resistencias[0]
    for resistencia in lista_resistencias:
        if resistencia["valor"] > mayor["valor"]:
            mayor = resistencia
        if resistencia["valor"] < menor["valor"]:
            menor = resistencia
    return mayor, menor


def calcular_promedio(lista_resistencias):
    suma = 0
    for resistencia in lista_resistencias:
        suma = suma + resistencia["valor"]
    return suma / len(lista_resistencias)


def contar_en_rango(lista_resistencias):
    cantidad = 0
    for resistencia in lista_resistencias:
        if RANGO_MINIMO <= resistencia["valor"] <= RANGO_MAXIMO:
            cantidad = cantidad + 1
    return cantidad


def calcular_porcentaje_en_rango(lista_resistencias):
    cantidad = contar_en_rango(lista_resistencias)
    return cantidad / len(lista_resistencias) * 100


def grafico_barras_valores(lista_resistencias):
    codigos = []
    valores = []
    for resistencia in lista_resistencias:
        codigos.append(resistencia["codigo"])
        valores.append(resistencia["valor"])
    plt.figure()
    plt.bar(codigos, valores, label="Valor en ohmios")
    plt.yscale("log")
    plt.title("Valor de cada resistencia")
    plt.xlabel("Código de la resistencia")
    plt.ylabel("Valor (Ω, escala log)")
    plt.legend()
    plt.show()


def grafico_torta_rango(lista_resistencias):
    dentro = contar_en_rango(lista_resistencias)
    fuera = len(lista_resistencias) - dentro
    plt.figure()
    plt.pie([dentro, fuera], labels=["Dentro del rango", "Fuera del rango"], autopct="%1.1f%%")
    plt.title("Resistencias dentro y fuera de [5.400 Ω, 6.200.000 Ω]")
    plt.show()
