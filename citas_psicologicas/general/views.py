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


# -------------------------------------------------------------
# Inicio de sesión general
# -------------------------------------------------------------
def login_inicio_sesion(request):
    """
    Permite a los usuarios iniciar sesión según su rol.
    Redirige a la sección correspondiente (cliente, profesional u organización).
    """
    mensaje = None

    # Diccionario de rutas por rol
    menu = {
        'cliente': 'cliente:mis_citas_option',
        'profesional': 'profesional:campanias_puntuales_option',
        'organizacion': 'general:login_registro_organizacion'
    }

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        usuario = authenticate(request, username=email, password=password)

        if usuario:
            login(request, usuario)  # Establece la sesión de Django

            # Verifica el rol y redirige según corresponda
            for m in menu:
                if usuario.rol and usuario.rol.nombre == m:
                    estado = False
                    try:
                        if (
                            usuario.profesional and
                            usuario.profesional.especialidad and
                            usuario.profesional.especialidad.nombre == "Neurología"
                        ):
                            estado = False
                    except AttributeError:
                        pass

                    # Guarda en sesión el estado del modelo predictivo
                    request.session['modelo_predictivo'] = estado

                    return redirect(menu[m])
        else:
            mensaje = "El usuario no existe o la contraseña es incorrecta."
    
    print("MENSAJE LOGIN:", mensaje)


    return render(
        request,
        'general/login/inicio_sesion/login_iniciar_sesion.html',
        {'mensaje': mensaje}
    )


# -------------------------------------------------------------
# Cerrar sesión general
# -------------------------------------------------------------
def logout_view(request):
    """Cierra la sesión actual y redirige al login general."""
    # Limpia la sesión y desconecta al usuario
    logout(request)

    # (Opcional) Limpia cualquier dato adicional guardado en la sesión
    request.session.flush()

    # Redirige al login principal
    return redirect('general:login_inicio_sesion')
