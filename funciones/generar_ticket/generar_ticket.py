import datetime

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