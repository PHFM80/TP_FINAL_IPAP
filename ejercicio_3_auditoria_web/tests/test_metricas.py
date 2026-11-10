import pytest

from ejercicio_3_auditoria_web.metricas import obtener_metricas_consumo


def test_total_emisiones():
    registros = [
        {"planta": "Norte", "consumo_kwh": 1000},
        {"planta": "Sur", "consumo_kwh": 2000},
    ]

    resultado = obtener_metricas_consumo(registros)

    assert resultado["total_emisiones"] == 1200.0


def test_planta_mayor_consumo():
    registros = [
        {"planta": "Norte", "consumo_kwh": 1500},
        {"planta": "Sur", "consumo_kwh": 2300},
        {"planta": "Oeste", "consumo_kwh": 3200},
    ]

    resultado = obtener_metricas_consumo(registros)

    assert resultado["planta_mayor_consumo"] == "Oeste"


def test_consumo_acumulado_por_planta():
    registros = [
        {"planta": "Norte", "consumo_kwh": 1500},
        {"planta": "Sur", "consumo_kwh": 2300},
        {"planta": "Norte", "consumo_kwh": 1200},
    ]

    resultado = obtener_metricas_consumo(registros)

    assert resultado["consumo_por_planta"]["Norte"] == 2700


def test_emisiones_por_planta():
    registros = [
        {"planta": "Norte", "consumo_kwh": 1000},
        {"planta": "Sur", "consumo_kwh": 2000},
    ]

    resultado = obtener_metricas_consumo(registros)

    assert resultado["emisiones_por_planta"]["Norte"] == 400.0
    assert resultado["emisiones_por_planta"]["Sur"] == 800.0


def test_lista_vacia():
    resultado = obtener_metricas_consumo([])

    assert resultado["total_emisiones"] == 0.0
    assert resultado["planta_mayor_consumo"] is None
    assert resultado["consumo_por_planta"] == {}
    assert resultado["emisiones_por_planta"] == {}


def test_consumo_negativo():
    registros = [
        {"planta": "Norte", "consumo_kwh": -100}
    ]

    with pytest.raises(ValueError):
        obtener_metricas_consumo(registros)