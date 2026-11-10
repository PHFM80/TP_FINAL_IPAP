
from ejercicio_3_auditoria_web.emisiones import calcular_emisiones_carbono


def obtener_metricas_consumo(registros):
    """
    Procesa los consumos de las plantas industriales.

    Retorna:
        - Total global de emisiones.
        - Planta de mayor consumo.
        - Consumo total por planta.
        - Emisiones totales por planta.
    """

    consumo_por_planta = {}
    emisiones_por_planta = {}

    total_emisiones = 0.0

    for registro in registros:

        planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        emisiones = calcular_emisiones_carbono(consumo)

        consumo_por_planta[planta] = (
            consumo_por_planta.get(planta, 0) + consumo
        )

        emisiones_por_planta[planta] = (
            emisiones_por_planta.get(planta, 0) + emisiones
        )

        total_emisiones += emisiones

    if consumo_por_planta:
        planta_mayor_consumo = max(
            consumo_por_planta,
            key=consumo_por_planta.get
        )
    else:
        planta_mayor_consumo = None

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "consumo_por_planta": consumo_por_planta,
        "emisiones_por_planta": emisiones_por_planta
    }
