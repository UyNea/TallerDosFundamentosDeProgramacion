from calculos import (crear_tabla_subregiones, crear_matriz_temperaturas, crear_tabla_paralela,
                      promedio_por_subregion, promedio_por_mes, promedio_departamento, MESES, SUBREGIONES,
                      grafico_barras_promedio_subregion, grafico_lineas_promedio_mes, grafico_barras_municipios)


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


matriz = None
opcion = ""

while opcion != "8":
    print("\n===== TEMPERATURAS DE LAS SUBREGIONES DE ANTIOQUIA =====")
    print("1. Generar temperaturas (pide N meses)")
    print("2. Ver estructura de subregiones (nombre, código, municipios)")
    print("3. Ver subregiones y temperaturas en paralelo")
    print("4. Ver promedio de cada subregión")
    print("5. Ver promedio de cada mes")
    print("6. Ver promedio de todo el departamento")
    print("7. Ver gráficos")
    print("8. Salir")
    opcion = input("Seleccione una opción (1 a 8): ")

    if opcion == "1":
        n_meses = leer_entero("Ingrese N, el número de meses (1 a 12): ", 1, 12)
        matriz = crear_matriz_temperaturas(n_meses)
        print("Temperaturas generadas correctamente.")
    elif opcion == "2":
        print(crear_tabla_subregiones())
    elif opcion in ["3", "4", "5", "6", "7"] and matriz is None:
        print("Primero debe generar las temperaturas (opción 1).")
    elif opcion == "3":
        print(crear_tabla_paralela(matriz))
    elif opcion == "4":
        promedios = promedio_por_subregion(matriz)
        for i in range(len(promedios)):
            print(SUBREGIONES[i][0], ":", round(promedios[i], 2), "°C")
    elif opcion == "5":
        promedios = promedio_por_mes(matriz)
        for j in range(len(promedios)):
            print(MESES[j], ":", round(promedios[j], 2), "°C")
    elif opcion == "6":
        print("Promedio de Antioquia:", round(promedio_departamento(matriz), 2), "°C")
    elif opcion == "7":
        grafico_barras_promedio_subregion(promedio_por_subregion(matriz))
        grafico_lineas_promedio_mes(promedio_por_mes(matriz))
        grafico_barras_municipios()
    elif opcion == "8":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
