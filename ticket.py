# Aplicación para generar tickets de compra en Python
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

# Ejemplo de uso
productos = ["Manzana", "Pan", "Leche"]
precios = [1.00, 2.50, 1.80]
cantidades = [3, 1, 2]

ticket = generar_ticket(productos, precios, cantidades)
print(ticket)