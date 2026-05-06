from django.shortcuts import render

# -------------------------------------------------------------
# Página principal
# -------------------------------------------------------------
def main_content_page(request):
    """Renderiza la página principal del sistema."""
    return render(request, 'general/main_page_citas.html')