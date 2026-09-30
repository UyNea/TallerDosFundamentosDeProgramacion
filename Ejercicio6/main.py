from calculos import (crear_matriz, extraer_diagonal_principal, extraer_diagonal_secundaria,
                      calcular_estadisticas, grafico_puntos, grafico_lineas)


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

while opcion != "6":
    print("\n===== MATRIZ CUADRADA Y DIAGONALES =====")
    print("1. Generar matriz n x n")
    print("2. Mostrar la matriz")
    print("3. Ver diagonal principal y secundaria")
    print("4. Ver estadísticas de la matriz (describe)")
    print("5. Ver gráficos")
    print("6. Salir")
    opcion = input("Seleccione una opción (1 a 6): ")

    if opcion == "1":
        n = leer_entero("Ingrese n (n >= 2): ", 2)
        matriz = crear_matriz(n)
        print("Matriz generada correctamente.")
    elif opcion in ["2", "3", "4", "5"] and matriz is None:
        print("Primero debe generar la matriz (opción 1).")
    elif opcion == "2":
        print(matriz)
    elif opcion == "3":
        print("Diagonal principal:", extraer_diagonal_principal(matriz))
        print("Diagonal secundaria:", extraer_diagonal_secundaria(matriz))
    elif opcion == "4":
        print(calcular_estadisticas(matriz))
    elif opcion == "5":
        principal = extraer_diagonal_principal(matriz)
        secundaria = extraer_diagonal_secundaria(matriz)
        grafico_puntos(principal, secundaria)
        grafico_lineas(principal, secundaria)
    elif opcion == "6":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
