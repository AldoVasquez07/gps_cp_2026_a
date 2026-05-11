from django.contrib import admin
from .models import (
    Pais, Ciudad, Rol, Usuario,
    LogProcesos, RegistroAcceso,
    AspectosNegocio, Disponibilidad
)

# -------------------------------------------------------------------
# MODELOS BÁSICOS
# -------------------------------------------------------------------

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'flag', 'created_date')
    search_fields = ('nombre', 'codigo')
    list_filter = ('flag',)
    ordering = ('nombre',)


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'flag', 'created_date')
    search_fields = ('nombre',)
    list_filter = ('pais', 'flag')
    ordering = ('nombre',)


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'flag', 'created_date')
    search_fields = ('nombre',)
    ordering = ('nombre',)

# -------------------------------------------------------------------
# USUARIO PERSONALIZADO
# -------------------------------------------------------------------

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'apellido_paterno', 'apellido_materno',
        'documento_identidad', 'rol', 'ciudad', 'flag'
    )
    search_fields = ('email', 'first_name', 'apellido_paterno', 'documento_identidad')
    list_filter = ('rol', 'ciudad', 'flag')
    ordering = ('email',)
    filter_horizontal = ()  # puedes agregar grupos o permisos si los usas
