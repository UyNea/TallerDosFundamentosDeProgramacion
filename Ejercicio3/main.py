from calculos import (calcular_valor_ohmios, formatear_ohmios, buscar_mayor_menor, calcular_promedio,
                      calcular_porcentaje_en_rango, grafico_barras_valores, grafico_torta_rango)


def leer_entero(mensaje, minimo, maximo=None):
    while True:
        texto = input(mensaje)
        try:
            numero = int(texto)
        except ValueError:
            print("Error: debe escribir un número entero.")
            continue
        if numero < minimo or (maximo is not None and numero > maximo):
            print("Error: valor fuera de rango (mínimo", minimo, "máximo", maximo, ").")
        else:
            return numero


def leer_codigo(codigos_usados):
    while True:
        codigo = input("Código de la resistencia (ej: R1): ").strip()
        if codigo == "":
            print("Error: el código no puede estar vacío.")
        elif codigo in codigos_usados:
            print("Error: ese código ya fue ingresado.")
        else:
            return codigo


def ingresar_resistencias():
    lista = []
    codigos_usados = []
    n = leer_entero("¿Cuántas resistencias desea procesar? (n >= 1): ", 1)
    for i in range(n):
        print("\n--- Resistencia", i + 1, "de", n, "---")
        codigo = leer_codigo(codigos_usados)
        banda1 = leer_entero("Valor de la 1ª banda (0 a 9): ", 0, 9)
        banda2 = leer_entero("Valor de la 2ª banda (0 a 9): ", 0, 9)
        banda3 = leer_entero("Valor de la 3ª banda, exponente (0 a 9): ", 0, 9)
        valor = calcular_valor_ohmios(banda1, banda2, banda3)
        resistencia = {"codigo": codigo, "banda1": banda1, "banda2": banda2, "banda3": banda3, "valor": valor}
        lista.append(resistencia)
        codigos_usados.append(codigo)
        print("Valor calculado:", valor, "Ω =", formatear_ohmios(valor))
    return lista


resistencias = []
opcion = ""

while opcion != "6":
    print("\n===== RESISTENCIAS ELÉCTRICAS =====")
    print("1. Ingresar resistencias")
    print("2. Ver resistencia mayor y menor")
    print("3. Ver promedio en ohmios")
    print("4. Ver porcentaje dentro del rango [5.400 Ω, 6.200.000 Ω]")
    print("5. Ver gráficos")
    print("6. Salir")
    opcion = input("Seleccione una opción (1 a 6): ")

    if opcion == "1":
        resistencias = ingresar_resistencias()
    elif opcion in ["2", "3", "4", "5"] and len(resistencias) == 0:
        print("Primero debe ingresar las resistencias (opción 1).")
    elif opcion == "2":
        mayor, menor = buscar_mayor_menor(resistencias)
        print("Mayor:", mayor["codigo"], "con", mayor["valor"], "Ω")
        print("Menor:", menor["codigo"], "con", menor["valor"], "Ω")
    elif opcion == "3":
        print("Promedio:", calcular_promedio(resistencias), "Ω")
    elif opcion == "4":
        print("Porcentaje en rango:", calcular_porcentaje_en_rango(resistencias), "%")
    elif opcion == "5":
        grafico_barras_valores(resistencias)
        grafico_torta_rango(resistencias)
    elif opcion == "6":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
