import datetime
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def cargar_productos_json():
    try:
        with open("productos_unicos.json", "r") as archivo:
            productos = json.load(archivo)
            print("Productos cargados correctamente desde 'productos_unicos.json'.")
            return productos
    except FileNotFoundError:
        print("El archivo 'productos_unicos.json' no fue encontrado.")
        return {}

def generar_ticket(productos_seleccionados):
    fecha_hora = datetime.datetime.now()
    encabezado_ticket = f"--- TICKET DE COMPRA ---\nFecha y hora: {fecha_hora}\n\n"
    total = 0

    # Preparar datos estructurados
    encabezados = ["Producto", "Cantidad", "Precio (€)", "Subtotal (€)"]
    datos = []
    for producto in productos_seleccionados:
        subtotal = producto['precio'] * producto['cantidad']
        total += subtotal
        datos.append([producto['nombre'], str(producto['cantidad']), f"{producto['precio']:.2f} €", f"{subtotal:.2f} €"])
    return encabezado_ticket, encabezados, datos, total

def guardar_ticket_pdf(encabezado_ticket, encabezados, datos, total, nombre_archivo="ticket.pdf"):
    try:
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        c.setFont("Helvetica", 10)

        # Añadir encabezado del ticket
        y = 750  # Posición vertical inicial
        for linea in encabezado_ticket.split("\n"):
            c.drawString(50, y, linea)
            y -= 15  # Reducir posición vertical para la próxima línea

        y -= 15  # Separación extra antes de las tablas

        # Configurar posiciones para las columnas
        x_producto = 50
        x_cantidad = 250
        x_precio = 300
        x_subtotal = 400

        # Dibujar encabezados de las columnas
        c.drawString(x_producto, y, encabezados[0])
        c.drawString(x_cantidad, y, encabezados[1])
        c.drawString(x_precio, y, encabezados[2])
        c.drawString(x_subtotal, y, encabezados[3])
        y -= 20  # Reducir posición vertical

        # Dibujar línea separadora
        c.line(50, y, 500, y)
        y -= 20

        # Dibujar datos de las filas
        for fila in datos:
            c.drawString(x_producto, y, fila[0])
            c.drawString(x_cantidad, y, fila[1])
            c.drawString(x_precio, y, fila[2])
            c.drawString(x_subtotal, y, fila[3])
            y -= 20

        # Dibujar línea final
        c.line(50, y, 500, y)
        y -= 20

        # Dibujar total
        c.drawString(x_producto, y, "Total:")
        c.drawString(x_subtotal, y, f"{total:.2f} €")
        c.save()
        print(f"Ticket guardado correctamente en el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al guardar el ticket en PDF: {e}")

def seleccionar_productos(productos_json):
    productos_seleccionados = []

    while True:
        id_seleccionado = input("\nIngrese el ID del producto (o 'exit' para terminar): ")
        if id_seleccionado.lower() == "exit":
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
        encabezado_ticket, encabezados, datos, total = generar_ticket(productos_seleccionados)
        guardar_ticket_pdf(encabezado_ticket, encabezados, datos, total)
    else:
        print("No se seleccionaron productos.")
else:
    print("No se pudieron cargar los productos desde el archivo JSON.")