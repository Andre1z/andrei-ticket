import datetime
import json

def cargar_productos_json():
    try:
        with open("productos_unicos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo 'productos_unicos.json' no fue encontrado.")
        return {}

def generar_ticket(productos_seleccionados):
    fecha_hora = datetime.datetime.now()
    ticket = f"--- TICKET DE COMPRA ---\nFecha y hora: {fecha_hora}\n\n"
    total = 0

    ticket += "Producto\tCantidad\tPrecio\tSubtotal\n"
    ticket += "-" * 50 + "\n"

    for producto in productos_seleccionados:
        subtotal = producto['precio'] * producto['cantidad']
        total += subtotal
        ticket += f"{producto['nombre']}\t{producto['cantidad']}\t{producto['precio']:.2f}\t{subtotal:.2f}\n"

    ticket += "-" * 50 + "\n"
    ticket += f"Total:\t\t\t\t{total:.2f}\n"
    ticket += "-" * 50 + "\n"

    return ticket

def seleccionar_productos(productos_json):
    productos_seleccionados = []

    while True:
        print("\nLista de productos disponibles:")
        for id_producto, datos in productos_json.items():
            print(f"ID: {id_producto} - Nombre: {datos['nombre']} - Precio: {datos['precio']:.2f}")

        id_seleccionado = input("\nIngrese el ID del producto (o 'salir' para terminar): ")
        if id_seleccionado.lower() == "salir":
            break
        if id_seleccionado not in productos_json:
            print("ID no válido. Intente de nuevo.")
            continue

        cantidad = int(input(f"Ingrese la cantidad de '{productos_json[id_seleccionado]['nombre']}': "))
        producto = {
            "nombre": productos_json[id_seleccionado]["nombre"],
            "precio": productos_json[id_seleccionado]["precio"],
            "cantidad": cantidad
        }
        productos_seleccionados.append(producto)

    return productos_seleccionados

# Uso
print("Bienvenido al generador de tickets.")
productos_json = cargar_productos_json()
if productos_json:
    productos_seleccionados = seleccionar_productos(productos_json)
    if productos_seleccionados:
        ticket = generar_ticket(productos_seleccionados)
        print("\n", ticket)
    else:
        print("No se seleccionaron productos.")
else:
    print("No se pudieron cargar los productos desde el archivo JSON.")