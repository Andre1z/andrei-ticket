from tkinter import ttk

def configurar_estilos(style):
    style.configure("Valid.TEntry", fieldbackground="lightgreen")
    style.configure("Invalid.TEntry", fieldbackground="lightcoral")
    style.configure("Default.TEntry", fieldbackground="white")

    style.configure("BotonAmarillo.TButton", background="#FFD700", relief="flat")
    style.configure("BotonVerde.TButton", background="#32CD32", relief="flat")