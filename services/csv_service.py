from datetime import datetime

def guardar_gasto(descripcion, valor):

    fecha = datetime.now().strftime("%Y-%m-%d")

    with open("data/gastos.csv", "a", encoding="utf-8") as archivo:

        archivo.write(
            f"{fecha},{descripcion},{valor}\n"
        )