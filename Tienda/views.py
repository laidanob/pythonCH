from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Producto

def producto(request,nombre,precio):
    productos = []
    producto=Producto(nombre="Fotolibro", precio=3933, fecha=datetime.today().strftime("%D"))
    texto= (f"Producto creado. Nombre: {producto.nombre} - Precio$: {producto.precio} - Fecha Creacion: {producto.fecha}")
    producto.save
    # productos.append(producto)
    # variables = {"productos " : productos, "texto " : texto}
    return HttpResponse(texto)
