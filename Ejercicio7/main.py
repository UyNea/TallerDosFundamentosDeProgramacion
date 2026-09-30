from calculos import (crear_matriz, promedios_por_fila, promedios_por_columna, estadisticas_globales,
                      grafico_barras_filas, grafico_barras_columnas, grafico_mapa_calor)


def leer_entero(mensaje, minimo):
    while True:
        texto = input(mensaje)
        try:
            numero = int(texto)
        except ValueError:
            print("Error: debe escribir un número entero.")
            continue
        if numero < minimo:
            print("Error: el valor debe ser mayor o igual a", minimo)
        else:
            return numero


matriz = None
opcion = ""

while opcion != "7":
    print("\n===== MATRIZ RECTANGULAR: PROMEDIOS =====")
    print("1. Generar matriz n x m")
    print("2. Mostrar la matriz")
    print("3. Ver promedio de cada fila")
    print("4. Ver promedio de cada columna")
    print("5. Ver promedio, máximo y mínimo de la matriz")
    print("6. Ver gráficos")
    print("7. Salir")
    opcion = input("Seleccione una opción (1 a 7): ")

    if opcion == "1":
        n = leer_entero("Ingrese n, el número de filas (n >= 2): ", 2)
        m = leer_entero("Ingrese m, el número de columnas (m >= 2): ", 2)
        matriz = crear_matriz(n, m)
        print("Matriz generada correctamente.")
    elif opcion in ["2", "3", "4", "5", "6"] and matriz is None:
        print("Primero debe generar la matriz (opción 1).")
    elif opcion == "2":
        print(matriz)
    elif opcion == "3":
        prom_filas = promedios_por_fila(matriz)
        for i in range(len(prom_filas)):
            print("Fila", i + 1, ": promedio =", prom_filas[i])
    elif opcion == "4":
        prom_columnas = promedios_por_columna(matriz)
        for j in range(len(prom_columnas)):
            print("Columna", j + 1, ": promedio =", prom_columnas[j])
    elif opcion == "5":
        r = estadisticas_globales(matriz)
        print("Promedio de la matriz:", r["promedio"])
        print("Máximo:", r["maximo"], "en fila", r["fila_max"] + 1, "columna", r["col_max"] + 1)
        print("Mínimo:", r["minimo"], "en fila", r["fila_min"] + 1, "columna", r["col_min"] + 1)
    elif opcion == "6":
        grafico_barras_filas(promedios_por_fila(matriz))
        grafico_barras_columnas(promedios_por_columna(matriz))
        grafico_mapa_calor(matriz)
    elif opcion == "7":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
