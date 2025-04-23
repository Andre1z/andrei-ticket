import datetime
from tkinter import messagebox  # Importación agregada
from funciones.generar_ticket.guardar_ticket_pdf import guardar_ticket_pdf
import datetime

def generar_ticket(productos_seleccionados):
    fecha_hora = datetime.datetime.now()
    encabezado_ticket = f"--- TICKET DE COMPRA ---\nFecha y hora: {fecha_hora}\n\n"

    encabezados = ["Producto", "Cantidad", "Precio (€)", "Subtotal (€)"]
    datos = []
    total = 0

    for producto in productos_seleccionados:
        subtotal = producto['precio'] * producto['cantidad']
        total += subtotal
        datos.append([producto['nombre'], str(producto['cantidad']), f"{producto['precio']:.2f} €", f"{subtotal:.2f} €"])

    return encabezado_ticket, encabezados, datos, total