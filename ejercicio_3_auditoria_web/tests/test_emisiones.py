
import pytest

from ejercicio_3_auditoria_web.emisiones import (
    calcular_emisiones_carbono
)


def test_calculo_emisiones_valor_nominal():
    resultado = calcular_emisiones_carbono(100)

    assert resultado == 40.0


def test_calculo_emisiones_factor_personalizado():
    resultado = calcular_emisiones_carbono(100, 0.5)

    assert resultado == 50.0


def test_calculo_emisiones_consumo_cero():
    resultado = calcular_emisiones_carbono(0)

    assert resultado == 0.0


def test_calculo_emisiones_consumo_negativo():
    with pytest.raises(ValueError):
        calcular_emisiones_carbono(-100)


def test_calculo_emisiones_consumo_decimal():
    resultado = calcular_emisiones_carbono(125.5)

    assert resultado == pytest.approx(50.2)
