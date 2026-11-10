
import pytest

from ejercicio_1_sensores.sensores import (
    limpiar_registro_sensor,
    generar_resumen_sensores
)


# --------------------------------------------------
# PRUEBAS: limpiar_registro_sensor
# --------------------------------------------------

def test_eliminar_espacios_sensor_id():
    registro = {
        "sensor_id": " SENSOR-001 ",
        "temperatura": "24.5C",
        "ubicacion": "Planta Norte"
    }

    resultado = limpiar_registro_sensor(registro)

    assert resultado["sensor_id"] == "SENSOR-001"


@pytest.mark.parametrize(
    "temperatura_raw, temperatura_esperada",
    [
        ("24.5C", 24.5),
        ("32.8 °C", 32.8),
        ("21.4 C", 21.4),
        ("35,6 grados", 35.6),
        ("-5.5C", -5.5)
    ]
)
def test_normalizar_temperatura(temperatura_raw, temperatura_esperada):
    registro = {
        "sensor_id": "SENSOR-001",
        "temperatura": temperatura_raw,
        "ubicacion": "Planta Norte"
    }

    resultado = limpiar_registro_sensor(registro)

    assert resultado["temperatura"] == temperatura_esperada
    assert isinstance(resultado["temperatura"], float)


def test_ubicacion_por_defecto():
    registro = {
        "sensor_id": "SENSOR-001",
        "temperatura": "24.5C",
        "ubicacion": ""
    }

    resultado = limpiar_registro_sensor(registro)

    assert resultado["ubicacion"] == "Ubicación no registrada"


def test_temperatura_invalida():
    registro = {
        "sensor_id": "SENSOR-001",
        "temperatura": "sin lectura",
        "ubicacion": "Planta Norte"
    }

    with pytest.raises(ValueError):
        limpiar_registro_sensor(registro)


def test_registro_sin_ubicacion():
    registro = {
        "sensor_id": "SENSOR-001",
        "temperatura": "24.5C"
    }

    resultado = limpiar_registro_sensor(registro)

    assert resultado["ubicacion"] == "Ubicación no registrada"


# --------------------------------------------------
# PRUEBAS: generar_resumen_sensores
# --------------------------------------------------

def test_detectar_sensores_en_alerta():
    sensores = [
        {"sensor_id": "SENSOR-001", "temperatura": 24.5},
        {"sensor_id": "SENSOR-002", "temperatura": 32.8},
        {"sensor_id": "SENSOR-003", "temperatura": 28.3},
        {"sensor_id": "SENSOR-004", "temperatura": 35.6}
    ]

    alertas, promedio = generar_resumen_sensores(sensores, 30.0)

    assert alertas == ["SENSOR-002", "SENSOR-004"]


def test_calcular_promedio_temperaturas():
    sensores = [
        {"sensor_id": "SENSOR-001", "temperatura": 20.0},
        {"sensor_id": "SENSOR-002", "temperatura": 30.0},
        {"sensor_id": "SENSOR-003", "temperatura": 40.0}
    ]

    alertas, promedio = generar_resumen_sensores(sensores, 50.0)

    assert promedio == 30.0


def test_lista_sensores_vacia():
    alertas, promedio = generar_resumen_sensores([], 30.0)

    assert alertas == []
    assert promedio == 0.0


def test_temperatura_igual_al_umbral_no_genera_alerta():
    sensores = [
        {"sensor_id": "SENSOR-001", "temperatura": 30.0}
    ]

    alertas, promedio = generar_resumen_sensores(sensores, 30.0)

    assert alertas == []
