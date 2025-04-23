import json
import random

def generar_nombres_unicos(cantidad):
    productos = {}
    palabras_base = ["Teclado", "Ratón", "Monitor", "Impresora", "Disco Duro", "Memoria RAM", "Placa Base", "Procesador", "Tarjeta Gráfica", "Fuente de Alimentación"]
    adjetivos = ["Pro", "Ultra", "Max", "Plus", "Elite", "Advance", "Smart", "Eco", "Turbo", "Prime"]

    for _ in range(cantidad):
        producto_id = f"{random.randint(100000, 999999)}"
        nombre = f"{random.choice(adjetivos)} {random.choice(palabras_base)} {random.randint(1, 100)}"
        precio = round(random.uniform(20, 500), 2)
        productos[producto_id] = {"nombre": nombre, "precio": precio}

    return productos

# Generar 2000 productos únicos
productos = generar_nombres_unicos(2000)

# Guardar en un archivo JSON
with open("productos_unicos.json", "w") as archivo:
    json.dump(productos, archivo, indent=4)

print("Lista de 2000 productos únicos generada y guardada en 'productos_unicos.json'.")