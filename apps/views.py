
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def inicio(request):
    return render(request, 'catalogo.html')