
import json
from pathlib import Path

from ejercicio_2_productos.modelos import (
    DispositivoEcológico,
    PanelSolar,
    StockInvalidoError
)


class GestorInventario:
    """Administra y persiste el catálogo de dispositivos."""

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        """
        Serializa los dispositivos y guarda el catálogo en JSON.
        """

        datos = [
            dispositivo.to_dict()
            for dispositivo in lista_dispositivos
        ]

        ruta = Path(ruta_archivo)
        ruta.parent.mkdir(parents=True, exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print(f"Catálogo guardado correctamente en: {ruta}")


def cargar_datos_prueba():
    """Carga los productos desde el archivo JSON."""

    ruta = Path(__file__).parent / "datos_prueba.json"

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


# --------------------------------------------------
# BLOQUE DE EJECUCIÓN
# --------------------------------------------------

if __name__ == "__main__":

    datos = cargar_datos_prueba()

    dispositivos = []

    # Creación de productos válidos
    for producto in datos["productos"]:

        dispositivo = PanelSolar(
            nombre=producto["nombre"],
            marca=producto["marca"],
            stock=producto["stock"],
            potencia_w=producto["potencia_w"],
            eficiencia=producto["eficiencia"]
        )

        dispositivos.append(dispositivo)

    # Demostración de excepción personalizada
    print("\n=== CONTROL DE INVENTARIO ===")

    try:
        dispositivos[0].stock = -10

    except StockInvalidoError as error:
        print(f"Error controlado: {error}")

    # Demostración de polimorfismo
    print("\n=== FICHAS TÉCNICAS ===")

    for dispositivo in dispositivos:
        print()
        print(dispositivo.ficha_tecnica())

    # Exportación del catálogo
    gestor = GestorInventario()

    ruta_catalogo = Path(__file__).parent / "catalogo_ecotech.json"

    gestor.guardar_catalogo_json(
        dispositivos,
        ruta_catalogo
    )
