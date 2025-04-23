# Generador de Tickets de Compra

Este proyecto es una aplicación de Python con interfaz gráfica creada usando **Tkinter**, diseñada para gestionar productos, generar tickets de compra en formato PDF y tener una estructura modular para facilitar la escalabilidad y el mantenimiento.

## Características del Proyecto

- **Interfaz gráfica**: Intuitiva y fácil de usar, creada con `Tkinter`.
- **Generación de tickets en PDF**: Los tickets se crean con detalles como productos, cantidades y totales usando `reportlab`.
- **Estilo visual personalizado**: Botones y colores armonizados con soporte para logotipo personalizado.
- **Arquitectura modular**: Código dividido en funciones independientes para una mejor organización.
- **Ícono personalizado**: Ventana con logotipo configurable para un toque profesional.

---

## Estructura del Proyecto

```plaintext
proyecto_ticket/
│── .gitattributes          # Configuración para el control de versiones
│── .gitignore              # Archivos y carpetas ignorados por Git
│── README.md               # Documentación del proyecto
│── generador.py            # Código del generador principal
│── ticket.py               # Módulo adicional para la generación de tickets (CLI)
│── ticket_grafico.py       # Archivo principal con la interfaz gráfica
│── productos_unicos.json   # Base de datos de productos
│── assets/                 # Carpeta para archivos de recursos
│   ├── logo.ico            # Ícono de la aplicación
│── funciones/              # Carpeta con todas las funciones organizadas
    ├── cargar/
    │   ├── cargar_productos.py  # Función para cargar productos del JSON
    ├── generar_ticket/
    │   ├── generar_ticket.py    # Función para generar el contenido del ticket
    │   ├── guardar_ticket_pdf.py # Función para guardar el ticket en formato PDF
    ├── interfaz/
    │   ├── añadir_producto.py   # Lógica para añadir productos
    │   ├── configurar_estilos.py # Configuración de estilos visuales
    │   ├── verificar_id.py      # Verificación del ID de productos (opcional)
```
## Instalación y Configuración
1. Clona este repositorio:
   ```bash
   git clone https://github.com/Andre1z/andrei-ticket.git
   cd andrei-ticket
   ```
2. Configura un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv env
   source env/bin/activate       # En Linux/MacOS
   .\env\Scripts\activate        # En Windows
   ```
3. Instala las dependencias necesarias:
   ```bash
   pip install reportlab
   ```
4. Asegúrate de tener el archivo productos_unicos.json configurado: Este archivo contiene los productos disponibles. Por ejemplo:
 ```json
   {
    "1": { "nombre": "Producto A", "precio": 10.50 },
    "2": { "nombre": "Producto B", "precio": 25.00 },
    "3": { "nombre": "Producto C", "precio": 15.75 }
  }
```
5. Coloca el archivo logo.ico dentro de la carpeta assets: Este archivo será el ícono de la ventana de la aplicación. Asegúrate de que esté en formato .ico.

## Uso de la Aplicación

1. Ejecuta el archivo principal con el siguiente comando:
   ```bash
   python ticket_grafico.py
   ```
2. En la interfaz gráfica:
   · ID del Producto: Introduce el ID de un producto existente en el archivo JSON.
   · Cantidad: Especifica cuántos quieres añadir.
   · Haz clic en Añadir Producto para agregarlo al ticket.
   · Haz clic en Generar Ticket (PDF) para guardar el ticket.
3. Salida del ticket (PDF): El archivo generado incluirá el encabezado, productos seleccionados, cantidades, precios y el total.

## Ejemplo de Ticket Generado

### El ticket generado en PDF tendrá el siguiente formato:
```txt
--- TICKET DE COMPRA ---
Fecha y hora: 2025-04-23 17:15:49.936587

Producto                 Cantidad  Precio (€)     Subtotal (€)
--------------------------------------------------------------
Producto A               2         10.50 €        21.00 €
Producto B               1         25.00 €        25.00 €
Producto C               3         15.75 €        47.25 €
--------------------------------------------------------------
Total:                                            93.25 €
--------------------------------------------------------------
```
## Contribuciones

### ¡Contribuciones son bienvenidas! Si tienes ideas para mejorar esta aplicación, abre un issue o envía un pull request.

## Licencia

### Este proyecto está bajo la Licencia MIT. Puedes usarlo libremente para propósitos personales y comerciales.

## Contacto

- **Autor**: Andrei Buga
- **Email**: bugaandrei1@gmail.com
- **GitHub**: https://github.com/Andre1z
