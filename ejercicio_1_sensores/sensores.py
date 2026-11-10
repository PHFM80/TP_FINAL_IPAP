
import json
import re
from pathlib import Path


def limpiar_registro_sensor(registro_raw):
    """
    Normaliza un registro crudo de un sensor.
    """

    sensor_id = str(registro_raw.get("sensor_id", "")).strip()

    temperatura_raw = str(registro_raw.get("temperatura", ""))

    coincidencia = re.search(r"[-+]?\d+(?:[.,]\d+)?", temperatura_raw)

    if not coincidencia:
        raise ValueError("La temperatura no contiene un valor numérico válido")

    temperatura = float(coincidencia.group().replace(",", "."))

    ubicacion = str(
        registro_raw.get("ubicacion") or "Ubicación no registrada"
    ).strip()

    if not ubicacion:
        ubicacion = "Ubicación no registrada"

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """
    Genera el listado de sensores en alerta y el promedio térmico.
    """

    lista_sensores_alerta = []

    if not lista_sensores_limpios:
        return lista_sensores_alerta, 0.0

    temperaturas = []

    for sensor in lista_sensores_limpios:

        temperatura = sensor["temperatura"]
        temperaturas.append(temperatura)

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    promedio_temperatura = sum(temperaturas) / len(temperaturas)

    return lista_sensores_alerta, promedio_temperatura


def cargar_datos_prueba():
    """
    Carga los registros desde el archivo JSON.
    """

    ruta_archivo = Path(__file__).parent / "datos_prueba.json"

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


# --------------------------------------------------
# BLOQUE DE EJECUCIÓN
# --------------------------------------------------

if __name__ == "__main__":

    datos = cargar_datos_prueba()

    registros_crudos = datos["sensores"]
    umbral = datos["umbral_temperatura"]

    # Normalización de registros
    sensores_limpios = []

    for registro in registros_crudos:
        sensor_limpio = limpiar_registro_sensor(registro)
        sensores_limpios.append(sensor_limpio)

    # Generación del resumen
    sensores_alerta, promedio = generar_resumen_sensores(
        sensores_limpios,
        umbral
    )

    # Reporte final
    print("\n========== ECOTECH SOLUTIONS ==========")
    print("       REPORTE DE SENSORES")
    print("=======================================")

    print(f"\nSensores procesados: {len(sensores_limpios)}")
    print(f"Umbral de temperatura: {umbral} °C")

    print("\nSensores normalizados:")

    for sensor in sensores_limpios:
        print(
            f"{sensor['sensor_id']} | "
            f"{sensor['temperatura']} °C | "
            f"{sensor['ubicacion']}"
        )

    print("\nSensores en alerta:")

    for sensor_id in sensores_alerta:
        print(f"- {sensor_id}")

    print(f"\nPromedio térmico: {promedio:.2f} °C")
    print("=======================================")
