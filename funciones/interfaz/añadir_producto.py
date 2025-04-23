from tkinter import messagebox

def añadir_producto(id_entry, cantidad_entry, productos, productos_seleccionados):
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
    id_entry.delete(0, "end")
    cantidad_entry.delete(0, "end")
    id_entry["style"] = "Default.TEntry"