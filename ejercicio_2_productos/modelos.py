
class StockInvalidoError(Exception):
    """Excepción para valores de stock negativos."""
    pass


class DispositivoEcológico:
    """Clase base para los dispositivos ecológicos."""

    def __init__(self, nombre, marca, stock):
        self.nombre = nombre
        self.marca = marca
        self.__stock = 0
        self.stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise TypeError("El stock debe ser un número entero.")

        if valor < 0:
            raise StockInvalidoError(
                "El stock no puede ser negativo."
            )

        self.__stock = valor

    def ficha_tecnica(self):
        """Devuelve la ficha técnica del dispositivo."""

        return (
            f"Dispositivo: {self.nombre}\n"
            f"Marca: {self.marca}\n"
            f"Stock disponible: {self.stock}"
        )

    def to_dict(self):
        """Convierte el dispositivo en un diccionario."""

        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "marca": self.marca,
            "stock": self.stock
        }


class PanelSolar(DispositivoEcológico):
    """Dispositivo especializado en generación solar."""

    def __init__(
        self,
        nombre,
        marca,
        stock,
        potencia_w,
        eficiencia
    ):
        super().__init__(nombre, marca, stock)

        self.potencia_w = potencia_w
        self.eficiencia = eficiencia

    def ficha_tecnica(self):
        """Personaliza la ficha técnica del panel solar."""

        return (
            f"=== FICHA TÉCNICA: PANEL SOLAR ===\n"
            f"Nombre: {self.nombre}\n"
            f"Marca: {self.marca}\n"
            f"Potencia: {self.potencia_w} W\n"
            f"Eficiencia: {self.eficiencia}%\n"
            f"Stock disponible: {self.stock}\n"
            f"=================================="
        )

    def to_dict(self):
        """Agrega los atributos específicos del panel solar."""

        datos = super().to_dict()

        datos.update({
            "potencia_w": self.potencia_w,
            "eficiencia": self.eficiencia
        })

        return datos
