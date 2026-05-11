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
