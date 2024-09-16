from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingresar/', views.ingresar_usuario, name='ingresar'),
    path('lista/', views.lista_usuarios, name='lista'),
]