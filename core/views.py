from django.shortcuts import render
from .models import vehiculo

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def form(request):
    return render(request,'core/form.html')

def create(request):
    return render(request,'core/create.html')


class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


def home(request):
    vehiculos = vehiculo.objects.all()
    datos = {
        "vehiculos":vehiculos
    }

