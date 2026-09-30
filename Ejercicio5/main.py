from calculos import (crear_dataframe, calcular_estadisticas, calcular_total_por_maquina, calcular_total_empresa,
                      grafico_barras_maquina_3, grafico_lineas_todas, grafico_barras_total_anual)

tabla = crear_dataframe()
opcion = ""

while opcion != "5":
    print("\n===== PRODUCCIÓN MENSUAL DE MÁQUINAS =====")
    print("1. Ver la tabla de producción")
    print("2. Ver estadísticas básicas de cada máquina (describe)")
    print("3. Ver total anual por máquina y total de la empresa")
    print("4. Ver gráficos")
    print("5. Salir")
    opcion = input("Seleccione una opción (1 a 5): ")

    if opcion == "1":
        print(tabla)
    elif opcion == "2":
        print(calcular_estadisticas(tabla))
    elif opcion == "3":
        print("Total anual por máquina:")
        print(calcular_total_por_maquina(tabla))
        print("Total de la empresa en el año:", calcular_total_empresa(tabla), "unidades")
    elif opcion == "4":
        grafico_barras_maquina_3(tabla)
        grafico_lineas_todas(tabla)
        grafico_barras_total_anual(tabla)
    elif opcion == "5":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
