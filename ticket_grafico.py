import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
import json

# Función para cargar los productos desde el archivo JSON
def cargar_productos_json():
    try:
        with open("productos_unicos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo 'productos_unicos.json' no fue encontrado.")
        return {}

# Función para guardar el ticket en PDF
def guardar_ticket_pdf(encabezado_ticket, encabezados, datos, total, nombre_archivo="ticket.pdf"):
    try:
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        c.setFont("Helvetica", 10)
        y = 750

        # Añadir encabezado del ticket
        for linea in encabezado_ticket.split("\n"):
            c.drawString(50, y, linea)
            y -= 15

        y -= 15

        # Posiciones de columnas
        x_producto = 50
        x_cantidad = 250
        x_precio = 300
        x_subtotal = 400

        # Dibujar encabezados
        c.drawString(x_producto, y, encabezados[0])
        c.drawString(x_cantidad, y, encabezados[1])
        c.drawString(x_precio, y, encabezados[2])
        c.drawString(x_subtotal, y, encabezados[3])
        y -= 20
        c.line(50, y, 500, y)
        y -= 20

        # Dibujar datos
        for fila in datos:
            c.drawString(x_producto, y, fila[0])
            c.drawString(x_cantidad, y, fila[1])
            c.drawString(x_precio, y, fila[2])
            c.drawString(x_subtotal, y, fila[3])
            y -= 20

        c.line(50, y, 500, y)
        y -= 20

        # Dibujar total
        c.drawString(x_producto, y, "Total:")
        c.drawString(x_subtotal, y, f"{total:.2f} €")
        c.save()
        messagebox.showinfo("Éxito", f"Ticket guardado correctamente en '{nombre_archivo}'.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el ticket en PDF: {e}")

# Función para generar el ticket y guardarlo en PDF
def generar_ticket():
    global productos_seleccionados
    if not productos_seleccionados:
        messagebox.showerror("Error", "No se han seleccionado productos.")
        return

    fecha_hora = datetime.datetime.now()
    encabezado_ticket = f"--- TICKET DE COMPRA ---\nFecha y hora: {fecha_hora}\n\n"

    encabezados = ["Producto", "Cantidad", "Precio (€)", "Subtotal (€)"]
    datos = []
    total = 0

    for producto in productos_seleccionados:
        subtotal = producto['precio'] * producto['cantidad']
        total += subtotal
        datos.append([producto['nombre'], str(producto['cantidad']), f"{producto['precio']:.2f} €", f"{subtotal:.2f} €"])

    guardar_ticket_pdf(encabezado_ticket, encabezados, datos, total)

# Función para verificar ID de producto y cambiar el color de la entrada
def verificar_id(event):
    producto_id = id_entry.get()
    if producto_id in productos:
        id_entry["style"] = "Valid.TEntry"
    else:
        id_entry["style"] = "Invalid.TEntry"

# Función para añadir un producto a la lista seleccionada
def añadir_producto():
    global productos_seleccionados
    producto_id = id_entry.get()
    cantidad = cantidad_entry.get()

    if producto_id not in productos:
        messagebox.showerror("Error", "ID de producto no válido.")
        return

    if not cantidad.isdigit() or int(cantidad) <= 0:
        messagebox.showerror("Error", "La cantidad debe ser un número entero positivo.")
        return

    cantidad = int(cantidad)
    producto = {
        "nombre": productos[producto_id]["nombre"],
        "precio": productos[producto_id]["precio"],
        "cantidad": cantidad
    }
    productos_seleccionados.append(producto)
    messagebox.showinfo("Éxito", f"Se añadió '{producto['nombre']}' correctamente.")
    id_entry.delete(0, tk.END)
    cantidad_entry.delete(0, tk.END)
    id_entry["style"] = "Default.TEntry"

# Cargar productos desde el JSON
productos = cargar_productos_json()
productos_seleccionados = []

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Generador de Tickets de Compra")
ventana.geometry("320x220")  # Tamaño más compacto
ventana.configure(bg="#E6F5D0")  # Fondo verde pastel suave

# Configurar estilos personalizados
style = ttk.Style()
style.configure("Valid.TEntry", fieldbackground="lightgreen")
style.configure("Invalid.TEntry", fieldbackground="lightcoral")
style.configure("Default.TEntry", fieldbackground="white")

style.configure("BotonAmarillo.TButton", background="#FFD700", relief="flat")
style.configure("BotonVerde.TButton", background="#32CD32", relief="flat")

# Etiquetas y entradas
ttk.Label(ventana, text="ID del Producto:", background="#E6F5D0").pack(fill="x", padx=10, pady=5)
id_entry = ttk.Entry(ventana, style="Default.TEntry")
id_entry.pack(fill="x", padx=10, pady=5)
id_entry.bind("<KeyRelease>", verificar_id)  # Verificar ID en tiempo real

ttk.Label(ventana, text="Cantidad:", background="#E6F5D0").pack(fill="x", padx=10, pady=5)
cantidad_entry = ttk.Entry(ventana)
cantidad_entry.pack(fill="x", padx=10, pady=5)

# Botones
añadir_button = ttk.Button(ventana, text="Añadir Producto", command=añadir_producto, style="BotonAmarillo.TButton")
añadir_button.pack(fill="x", padx=10, pady=10)

generar_button = ttk.Button(ventana, text="Generar Ticket (PDF)", command=generar_ticket, style="BotonVerde.TButton")
generar_button.pack(fill="x", padx=10, pady=10)

# Iniciar aplicación
ventana.mainloop()