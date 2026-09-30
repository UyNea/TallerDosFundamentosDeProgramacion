import matplotlib.pyplot as plt

MASA_MINIMA = 88.9
MASA_MAXIMA = 200.59


def buscar_extremos(lista_elementos, clave):
    mayor = lista_elementos[0]
    menor = lista_elementos[0]
    for elemento in lista_elementos:
        if elemento[clave] > mayor[clave]:
            mayor = elemento
        if elemento[clave] < menor[clave]:
            menor = elemento
    return mayor, menor


def calcular_masa_promedio(lista_elementos):
    suma = 0
    for elemento in lista_elementos:
        suma = suma + elemento["masa"]
    return suma / len(lista_elementos)


def contar_en_rango(lista_elementos):
    cantidad = 0
    for elemento in lista_elementos:
        if MASA_MINIMA <= elemento["masa"] <= MASA_MAXIMA:
            cantidad = cantidad + 1
    return cantidad


def calcular_porcentaje_en_rango(lista_elementos):
    return contar_en_rango(lista_elementos) / len(lista_elementos) * 100


def grafico_barras_masa(lista_elementos):
    simbolos = []
    masas = []
    for elemento in lista_elementos:
        simbolos.append(elemento["simbolo"])
        masas.append(elemento["masa"])
    plt.figure()
    plt.bar(simbolos, masas, label="Masa atómica")
    plt.title("Masa atómica por elemento")
    plt.xlabel("Símbolo químico")
    plt.ylabel("Masa atómica (uma)")
    plt.legend()
    plt.show()


def grafico_dispersion(lista_elementos):
    numeros = []
    masas = []
    for elemento in lista_elementos:
        numeros.append(elemento["numero_atomico"])
        masas.append(elemento["masa"])
    plt.figure()
    plt.scatter(numeros, masas, label="Elementos")
    for elemento in lista_elementos:
        plt.annotate(elemento["simbolo"], (elemento["numero_atomico"], elemento["masa"]))
    plt.title("Número atómico vs masa atómica")
    plt.xlabel("Número atómico")
    plt.ylabel("Masa atómica (uma)")
    plt.legend()
    plt.grid(True)
    plt.show()
