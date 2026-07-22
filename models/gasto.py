class Gasto:

    def __init__(self, fecha, descripcion, valor):

        self.fecha = fecha
        self.descripcion = descripcion
        self.valor = valor

    def mostrar(self):

        return (
            f"{self.fecha} - "
            f"{self.descripcion} - "
            f"${self.valor:,}"
        )