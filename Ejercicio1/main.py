from calculos import calcular_terminos, calcular_sumas_parciales, grafico_lineas_terminos, grafico_barras_parciales


def leer_entero(mensaje, minimo, maximo=None):
    while True:
        texto = input(mensaje)
        try:
            numero = int(texto)
        except ValueError:
            print("Error: debe escribir un número entero.")
            continue
        if numero < minimo:
            print("Error: el valor debe ser mayor o igual a", minimo)
        elif maximo is not None and numero > maximo:
            print("Error: el valor debe ser menor o igual a", maximo)
        else:
            return numero


print("Bienvenido al programa de la sumatoria con factoriales")
n = leer_entero("Ingrese n (1 a 15): ", 1, 15)
x = leer_entero("Ingrese x (entero mayor o igual a 1): ", 1)

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
    print("Error: con esos valores el resultado es demasiado grande. Pruebe con un x menor.")
