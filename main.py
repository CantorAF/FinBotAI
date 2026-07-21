print("================================")
print("       FinBot AI v0.6")
print("================================")

gastos = []

continuar = True

while continuar:

    print()
    print("1. Registrar gasto")
    print("2. Ver gastos")
    print("3. Ver total gastado")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        descripcion = input("Descripción del gasto: ")
        valor = int(input("Valor del gasto: "))

        gasto = {
            "descripcion": descripcion,
            "valor": valor
        }

        gastos.append(gasto)

        print("✅ Gasto registrado")

    if opcion == 2:

        print()
        print("LISTA DE GASTOS")

        for gasto in gastos:

            print(
                gasto["descripcion"],
                "- $",
                gasto["valor"]
            )

    if opcion == 3:

        total = 0

        for gasto in gastos:
            total = total + gasto["valor"]

        print()
        print("💰 Total gastado: $", total)

    if opcion == 4:

        continuar = False
        print("Hasta luego")