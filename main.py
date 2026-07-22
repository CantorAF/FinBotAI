from services.csv_service import guardar_gasto
from services.report_service import mostrar_historial

print("================================")
print("       FinBot AI v2.0")
print("================================")

continuar = True

while continuar:

    print()
    print("1. Registrar gasto")
    print("2. Ver historial")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        descripcion = input("Descripción del gasto: ")
        valor = int(input("Valor del gasto: "))

        guardar_gasto(descripcion, valor)

        print("✅ Gasto guardado")

    if opcion == 2:

        mostrar_historial()

    if opcion == 3:

        continuar = False

        print("Hasta luego")