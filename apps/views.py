from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista de registro
def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm()  # Instancia del formulario de creación de usuario
        })
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario si el formulario es válido
            return redirect(reverse('catalogo'))  # Redirige a la página del catálogo
        else:
            # Si el formulario no es válido, recarga la página de registro con los errores
            return render(request, 'registro.html', {
                'form': form
            })
