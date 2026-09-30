from calculos import (buscar_extremos, calcular_masa_promedio, calcular_porcentaje_en_rango,
                      grafico_barras_masa, grafico_dispersion)


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


def leer_real_positivo(mensaje):
    while True:
        texto = input(mensaje).replace(",", ".")
        try:
            numero = float(texto)
        except ValueError:
            print("Error: debe escribir un número real.")
            continue
        if numero > 0:
            return numero
        print("Error: la masa atómica debe ser mayor que 0.")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: no puede estar vacío.")


def leer_simbolo():
    while True:
        simbolo = input("Símbolo químico (ej: H, Br): ").strip()
        if simbolo.isalpha() and 1 <= len(simbolo) <= 3:
            return simbolo.capitalize()
        print("Error: el símbolo debe tener de 1 a 3 letras.")


def ingresar_elementos():
    lista = []
    n = leer_entero("¿Cuántos elementos desea procesar? (n >= 1): ", 1)
    for i in range(n):
        print("\n--- Elemento", i + 1, "de", n, "---")
        nombre = leer_texto("Nombre del elemento: ")
        simbolo = leer_simbolo()
        numero_atomico = leer_entero("Número atómico (1 a 118): ", 1, 118)
        masa = leer_real_positivo("Masa atómica (uma): ")
        elemento = {"nombre": nombre, "simbolo": simbolo, "numero_atomico": numero_atomico, "masa": masa}
        lista.append(elemento)
    return lista


elementos = []
opcion = ""

while opcion != "7":
    print("\n===== TABLA PERIÓDICA =====")
    print("1. Ingresar elementos")
    print("2. Ver mayor y menor masa atómica")
    print("3. Ver mayor y menor número atómico")
    print("4. Ver masa atómica promedio")
    print("5. Ver porcentaje con masa en [88.9, 200.59] uma")
    print("6. Ver gráficos")
    print("7. Salir")
    opcion = input("Seleccione una opción (1 a 7): ")

    if opcion == "1":
        elementos = ingresar_elementos()
    elif opcion in ["2", "3", "4", "5", "6"] and len(elementos) == 0:
        print("Primero debe ingresar los elementos (opción 1).")
    elif opcion == "2":
        mayor, menor = buscar_extremos(elementos, "masa")
        print("Mayor masa:", mayor["nombre"], "(" + mayor["simbolo"] + ") con", mayor["masa"], "uma")
        print("Menor masa:", menor["nombre"], "(" + menor["simbolo"] + ") con", menor["masa"], "uma")
    elif opcion == "3":
        mayor, menor = buscar_extremos(elementos, "numero_atomico")
        print("Mayor número atómico:", mayor["nombre"], "(" + mayor["simbolo"] + ") con", mayor["numero_atomico"])
        print("Menor número atómico:", menor["nombre"], "(" + menor["simbolo"] + ") con", menor["numero_atomico"])
    elif opcion == "4":
        print("Masa atómica promedio:", calcular_masa_promedio(elementos), "uma")
    elif opcion == "5":
        print("Porcentaje en rango:", calcular_porcentaje_en_rango(elementos), "%")
    elif opcion == "6":
        grafico_barras_masa(elementos)
        grafico_dispersion(elementos)
        print("Comentario: la masa atómica crece de forma aproximadamente lineal con el número atómico.")
    elif opcion == "7":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
