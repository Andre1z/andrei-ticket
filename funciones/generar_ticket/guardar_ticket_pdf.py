from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import messagebox  # Importación agregada

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