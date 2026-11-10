import json
from pathlib import Path

from django.shortcuts import render

from ejercicio_3_auditoria_web.metricas import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    ruta_datos = Path(__file__).parent / "datos_prueba.json"

    with open(ruta_datos, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    registros = datos["registros"]
    metricas = obtener_metricas_consumo(registros)

    filas_plantas = []

    for planta, consumo in metricas["consumo_por_planta"].items():
        filas_plantas.append({
            "planta": planta,
            "consumo": consumo,
            "emisiones": metricas["emisiones_por_planta"][planta],
        })

    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "filas_plantas": filas_plantas,
    }

    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )