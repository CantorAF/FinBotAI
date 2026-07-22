def mostrar_historial():

    total = 0

    print()
    print("===== HISTORIAL DE GASTOS =====")
    print()

    print(f"{'Fecha':<12} {'Descripción':<20} {'Valor':>12}")
    print("-" * 50)

    with open("data/gastos.csv", "r", encoding="utf-8") as archivo:

        for linea in archivo:

            fecha, descripcion, valor = linea.strip().split(",")

            valor = int(valor)

            total += valor

            print(
                f"{fecha:<12} {descripcion:<20} ${valor:>10,}"
            )

    print("-" * 50)
    print(f"TOTAL: ${total:,}")