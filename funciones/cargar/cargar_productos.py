import json
def cargar_productos_json():
    try:
        with open("productos_unicos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo 'productos_unicos.json' no fue encontrado.")
        return {}