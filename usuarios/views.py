from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def ingresar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = UsuarioForm()
    return render(request, 'ingresar.html', {'form': form})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista.html', {'usuarios': usuarios})