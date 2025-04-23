import json
import os

def cargar_productos():
    try:
        # Obtener la ruta absoluta del archivo JSON
        ruta_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../productos_unicos.json")

        # Cargar el archivo JSON
        with open(ruta_json, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo 'productos_unicos.json' no fue encontrado.")
        return {}