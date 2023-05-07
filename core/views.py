from django.shortcuts import render,redirect
from .models import Cliente
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def form(request):
    return render(request,'core/form.html')

def create(request):
    return render(request,'core/create.html')

def realizarregistro(request):
    nombre_c = request.POST['nombre']
    telefono_c = request.POST['telefono']
    correo_c = request.POST['correo']
    pass_c = request.POST['password']

    #insert en tabla
    Cliente.objects.create(nombreCliente = nombre_c,
                           telefonoCliente = telefono_c,
                           correoCliente = correo_c,
                           passCliente = pass_c)
    messages.success(request, 'Cliente registrado')
    return redirect('create')