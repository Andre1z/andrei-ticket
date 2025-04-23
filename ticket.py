import datetime

def generar_ticket(productos, precios, cantidades):
    fecha_hora = datetime.datetime.now()
    ticket = f"--- TICKET DE COMPRA ---\nFecha y hora: {fecha_hora}\n\n"
    total = 0

    ticket += "Producto\tCantidad\tPrecio\tSubtotal\n"
    ticket += "-" * 50 + "\n"

    for producto, precio, cantidad in zip(productos, precios, cantidades):
        subtotal = precio * cantidad
        total += subtotal
        ticket += f"{producto}\t{cantidad}\t{precio:.2f}\t{subtotal:.2f}\n"

    ticket += "-" * 50 + "\n"
    ticket += f"Total:\t\t\t\t{total:.2f}\n"
    ticket += "-" * 50 + "\n"

    return ticket

def ingresar_datos():
    productos = []
    precios = []
    cantidades = []

    while True:
        producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if producto.lower() == "salir":
            break
        precio = float(input(f"Ingrese el precio de {producto}: "))
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))

        productos.append(producto)
        precios.append(precio)
        cantidades.append(cantidad)

    return productos, precios, cantidades

# Uso
print("Bienvenido al generador de tickets.")
productos, precios, cantidades = ingresar_datos()
ticket = generar_ticket(productos, precios, cantidades)
print("\n", ticket)