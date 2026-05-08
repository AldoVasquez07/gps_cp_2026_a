from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente


# -------------------------------------------------------------
# Página principal del cliente (mis citas)
# -------------------------------------------------------------
@login_required
def mis_citas_option(request):
    """Muestra las citas del cliente autenticado."""
    cliente = Cliente.objects.get(usuario=request.user)
    return render(request, 'cliente/mis_citas.html', {'cliente': cliente})


# -------------------------------------------------------------
# Perfil del cliente
# -------------------------------------------------------------
@login_required
def perfil_cliente(request):
    """Muestra el perfil del cliente autenticado."""
    cliente = Cliente.objects.get(usuario=request.user)
    return render(request, 'cliente/perfil_cliente.html', {'cliente': cliente})


# -------------------------------------------------------------
# Editar perfil del cliente
# -------------------------------------------------------------
@login_required
def editar_perfil_cliente(request):
    """Permite editar los datos personales y clínicos del cliente."""
    cliente = Cliente.objects.get(usuario=request.user)

    if request.method == 'POST':
        cliente.nombres = request.POST.get('nombres')
        cliente.apellidos = request.POST.get('apellidos')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.save()
        return redirect('cliente:perfil_cliente')

    return render(request, 'cliente/editar_perfil.html', {'cliente': cliente})