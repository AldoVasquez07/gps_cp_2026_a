from django.shortcuts import render

# -------------------------------------------------------------
# Página principal
# -------------------------------------------------------------
def main_content_page(request):
    """Renderiza la página principal del sistema."""
    return render(request, 'general/main_page_citas.html')


# -------------------------------------------------------------
# Selección del tipo de usuario
# -------------------------------------------------------------
def seleccion_tipo_usuario(request):
    """Muestra la página para elegir el tipo de usuario (cliente, profesional)."""
    return render(request, 'general/seleccion_tipo_usuario.html')

