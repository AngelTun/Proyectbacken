"""
URL configuration for FARMACIAH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from apps import views  # Importa las vistas desde tu aplicación actual

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),  # Página principal (inicio.html)
    path('registro/', views.registro, name='registro'),  # Página de registro (registro.html)
    path('catalogo/', views.catalogo, name='catalogo'),  # Página de catálogo (catalogo.html)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Cerrar sesión
]
