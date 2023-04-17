from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def form(request):
    return render(request,'core/form.html')

def create(request):
    return render(request,'core/create.html')
