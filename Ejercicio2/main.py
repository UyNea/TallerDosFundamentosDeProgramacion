from calculos import calcular_terminos, calcular_sumas_parciales, grafico_lineas_terminos, grafico_barras_parciales


def leer_entero(mensaje, minimo, maximo):
    while True:
        texto = input(mensaje)
        try:
            numero = int(texto)
        except ValueError:
            print("Error: debe escribir un número entero.")
            continue
        if numero < minimo or numero > maximo:
            print("Error: el valor debe estar entre", minimo, "y", maximo)
        else:
            return numero


def leer_real(mensaje):
    while True:
        texto = input(mensaje).replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Error: debe escribir un número real.")


print("Bienvenido al programa de la sumatoria de Fibonacci sobre primos")
n = leer_entero("Ingrese n (1 a 10): ", 1, 10)
x = leer_real("Ingrese x (cualquier real): ")

try:
    terminos = calcular_terminos(x, n)
    parciales = calcular_sumas_parciales(terminos)
    print("\nTérminos de la sumatoria:")
    for i in range(len(terminos)):
        print("Término", i + 1, "=", terminos[i])
    print("\nEl valor de S es:", parciales[-1])
    grafico_lineas_terminos(terminos)
    grafico_barras_parciales(parciales)
except OverflowError:
    print("Error: con ese x el resultado es demasiado grande. Pruebe con un x menor.")
