
import json
import pytest

from ejercicio_2_productos.modelos import (
    DispositivoEcológico,
    PanelSolar,
    StockInvalidoError
)

from ejercicio_2_productos.inventario import GestorInventario


# --------------------------------------------------
# PRUEBAS: DISPOSITIVO ECOLÓGICO
# --------------------------------------------------

def test_crear_dispositivo():
    dispositivo = DispositivoEcológico(
        "Lámpara solar",
        "EcoTech",
        10
    )

    assert dispositivo.nombre == "Lámpara solar"
    assert dispositivo.marca == "EcoTech"
    assert dispositivo.stock == 10


def test_asignar_stock_valido():
    dispositivo = DispositivoEcológico(
        "Lámpara solar",
        "EcoTech",
        10
    )

    dispositivo.stock = 20

    assert dispositivo.stock == 20


def test_stock_negativo_genera_excepcion():
    with pytest.raises(StockInvalidoError):
        DispositivoEcológico(
            "Lámpara solar",
            "EcoTech",
            -5
        )


def test_asignar_stock_negativo():
    dispositivo = DispositivoEcológico(
        "Lámpara solar",
        "EcoTech",
        10
    )

    with pytest.raises(StockInvalidoError):
        dispositivo.stock = -5

    # El stock original debe mantenerse.
    assert dispositivo.stock == 10


def test_stock_no_entero():
    dispositivo = DispositivoEcológico(
        "Lámpara solar",
        "EcoTech",
        10
    )

    with pytest.raises(TypeError):
        dispositivo.stock = 5.5


# --------------------------------------------------
# PRUEBAS: PANEL SOLAR
# --------------------------------------------------

def test_crear_panel_solar():
    panel = PanelSolar(
        "Panel Eco 450",
        "EcoTech",
        15,
        450,
        21.5
    )

    assert panel.nombre == "Panel Eco 450"
    assert panel.stock == 15
    assert panel.potencia_w == 450
    assert panel.eficiencia == 21.5


def test_herencia_panel_solar():
    panel = PanelSolar(
        "Panel Eco 450",
        "EcoTech",
        15,
        450,
        21.5
    )

    assert isinstance(panel, DispositivoEcológico)


def test_polimorfismo_ficha_tecnica():
    panel = PanelSolar(
        "Panel Eco 450",
        "EcoTech",
        15,
        450,
        21.5
    )

    ficha = panel.ficha_tecnica()

    assert "PANEL SOLAR" in ficha
    assert "450 W" in ficha
    assert "21.5%" in ficha


def test_serializacion_panel_solar():
    panel = PanelSolar(
        "Panel Eco 450",
        "EcoTech",
        15,
        450,
        21.5
    )

    datos = panel.to_dict()

    assert datos["tipo"] == "PanelSolar"
    assert datos["potencia_w"] == 450
    assert datos["eficiencia"] == 21.5


# --------------------------------------------------
# PRUEBAS: GESTOR DE INVENTARIO
# --------------------------------------------------

def test_guardar_catalogo_json(tmp_path):
    panel = PanelSolar(
        "Panel Eco 450",
        "EcoTech",
        15,
        450,
        21.5
    )

    ruta = tmp_path / "catalogo_ecotech.json"

    gestor = GestorInventario()

    gestor.guardar_catalogo_json([panel], ruta)

    assert ruta.exists()

    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    assert len(datos) == 1
    assert datos[0]["nombre"] == "Panel Eco 450"
    assert datos[0]["stock"] == 15


def test_guardar_catalogo_vacio(tmp_path):
    ruta = tmp_path / "catalogo_ecotech.json"

    gestor = GestorInventario()

    gestor.guardar_catalogo_json([], ruta)

    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    assert datos == []
