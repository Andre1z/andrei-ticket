import tkinter as tk
from tkinter import ttk, messagebox
from funciones.cargar.cargar_productos import cargar_productos
from funciones.generar_ticket.generar_ticket import generar_ticket
from funciones.generar_ticket.guardar_ticket_pdf import guardar_ticket_pdf
from funciones.interfaz.añadir_producto import añadir_producto
from funciones.interfaz.configurar_estilos import configurar_estilos

# Configurar ventana principal
ventana = tk.Tk()
ventana.title("Ticket Generator")
ventana.geometry("320x220")  # Tamaño más compacto
ventana.configure(bg="#E6F5D0")  # Fondo verde pastel suave

# Configurar ícono de la aplicación
ventana.iconbitmap("assets/logo.ico")  # Ruta al archivo de ícono

# Configurar estilos personalizados
style = ttk.Style()
configurar_estilos(style)

# Cargar productos desde el JSON
productos = cargar_productos()
productos_seleccionados = []

# Crear etiquetas y entradas de texto
ttk.Label(ventana, text="ID del Producto:", background="#E6F5D0").pack(fill="x", padx=10, pady=5)
id_entry = ttk.Entry(ventana, style="Default.TEntry")
id_entry.pack(fill="x", padx=10, pady=5)

ttk.Label(ventana, text="Cantidad:", background="#E6F5D0").pack(fill="x", padx=10, pady=5)
cantidad_entry = ttk.Entry(ventana)
cantidad_entry.pack(fill="x", padx=10, pady=5)

# Botones de acción
ttk.Button(
    ventana, text="Añadir Producto",
    command=lambda: añadir_producto(id_entry, cantidad_entry, productos, productos_seleccionados),
    style="BotonAmarillo.TButton"
).pack(fill="x", padx=10, pady=10)

ttk.Button(
    ventana, text="Generar Ticket (PDF)",
    command=lambda: guardar_ticket_pdf(*generar_ticket(productos_seleccionados)),
    style="BotonVerde.TButton"
).pack(fill="x", padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()