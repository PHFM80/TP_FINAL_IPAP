
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """
    Calcula las emisiones de carbono según el consumo eléctrico.

    Args:
        consumo_kwh: Consumo eléctrico en kWh.
        factor_emision: Factor de emisión en kg de CO2 por kWh.

    Returns:
        Emisiones de carbono en kg de CO2.
    """

    if consumo_kwh < 0:
        raise ValueError("El consumo eléctrico no puede ser negativo.")

    return consumo_kwh * factor_emision
