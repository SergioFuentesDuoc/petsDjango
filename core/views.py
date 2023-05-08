from django.shortcuts import render,redirect
from .models import Cliente
from .models import Producto

from django.contrib import messages

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'core/home.html', data)

def form(request):
    return render(request,'core/form.html')

def create(request):
    return render(request,'core/create.html')

def realizarregistro(request):
    nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    correo = request.POST['correo']
    password = request.POST['password']

    #insert en tabla
    Cliente.objects.create(nombreCliente = nombre, telefonoCliente = telefono, correoCliente = correo, passCliente = password)
    messages.success(request, 'Cliente registrado')
    return redirect('create')






