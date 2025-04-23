def verificar_id(event):
    producto_id = id_entry.get()
    if producto_id in productos:
        id_entry["style"] = "Valid.TEntry"
    else:
        id_entry["style"] = "Invalid.TEntry"