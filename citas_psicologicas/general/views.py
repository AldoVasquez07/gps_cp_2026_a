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


# -------------------------------------------------------------
# Registro de clientes
# -------------------------------------------------------------
def login_registro_cliente(request):
    """
    Permite registrar un nuevo usuario con rol de cliente.
    Usa la misma estructura que el registro de profesional,
    pero adaptada a la lógica más simple de clientes.
    """
    ciudades = Ciudad.objects.filter(flag=True).order_by('nombre')
    mensaje = None

    if request.method == 'POST':
        # Obtener contraseñas desde el formulario
        password = request.POST.get('contrasena_cliente')
        confirm_password = request.POST.get('confirmar_contrasena_cliente')

        # Verificar coincidencia
        if password != confirm_password:
            mensaje = "Las contraseñas no coinciden."
        else:
            try:
                # Crear instancia del usuario (sin guardar aún)
                nuevo_usuario = Usuario(
                    first_name=request.POST.get('nombre_cliente'),
                    apellido_paterno=request.POST.get('apellido_paterno_cliente'),
                    apellido_materno=request.POST.get('apellido_materno_cliente'),
                    email=request.POST.get('correo_cliente'),
                    fecha_nacimiento=request.POST.get('fecha_nacimiento_cliente'),
                    documento_identidad=request.POST.get('documento_identidad_cliente'),
                    telefono=request.POST.get('telefono_cliente'),
                    ciudad=Ciudad.objects.filter(id=request.POST.get('ciudad_cliente')).first(),
                    rol=Rol.objects.filter(nombre='cliente').first()
                )

                # Asignar contraseña correctamente (usa hashing)
                nuevo_usuario.set_password(password)

                # Validar y guardar usuario
                nuevo_usuario.clean()
                nuevo_usuario.save()

                # Crear objeto Cliente asociado
                nuevo_cliente = Cliente(usuario=nuevo_usuario)
                nuevo_cliente.save()

                # Redirigir al inicio de sesión
                return redirect('general:login_inicio_sesion')

            except Exception as ex:
                mensaje = str(ex)

    # Si GET o error, renderizar nuevamente con contexto
    return render(
        request,
        'general/login/registro/login_registrar_cliente.html',
        {
            'ciudades': ciudades,
            'mensaje': mensaje
        }
    )
