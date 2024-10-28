from django.shortcuts import render
from .models import Cliente

# Create your views here.

def inicio_vista(request):
    Listadoclientes = Cliente.objects.all()
    return render(request,"base.html", {"losclientes":Listadoclientes})
