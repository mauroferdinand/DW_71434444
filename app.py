import streamlit as st

# Lista de categorías permitidas
categorias_permitidas = ["Chocolates", "Caramelos", "Mashmelos", "Galletas", "Salados", "Gomas de mascar"]

def validar_producto(nombre, precio, categorias, en_venta):
    if len(nombre) > 20:
        return "El nombre del producto no debe ser mayor a 20 caracteres."

    try:
        precio = float(precio)
        if precio < 0 or precio >= 1000:
            return "El precio del producto debe ser mayor a 0 y menor a 999 soles."
    except ValueError:
        return "Por favor verifique el campo del precio."

    if not categorias:
        return "El producto debe estar incluido en una o más categorías."

    if en_venta not in ["Sí", "No"]:
        return "Por favor seleccione si el producto está en venta o no."

    return "¡Felicidades su producto se agregó!"

# Título de la aplicación
st.title("Formulario de Producto")

# Campos del formulario
nombre = st.text_input("Nombre del Producto:")
precio = st.text_input("Precio del Producto:")
categorias = st.multiselect("Categorías del Producto:", categorias_permitidas)
en_venta = st.radio("¿El producto está en venta?", ["Sí", "No"])

# Botón para validar el producto
if st.button("Agregar Producto"):
    mensaje = validar_producto(nombre, precio, categorias, en_venta)
    if "Felicidades" in mensaje:
        st.success(mensaje)
    else:
        st.error(mensaje)
