from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'apellidos', 'nombres', 'dni',
        'telefono', 'especialidad_requerida', 'activo'
    )
    list_filter = ('activo', 'genero', 'especialidad_requerida')
    search_fields = ('nombres', 'apellidos', 'dni', 'email')
    ordering = ('apellidos', 'nombres')
    list_editable = ('activo',)
    readonly_fields = ('fecha_registro',)

    fieldsets = (
        ('Datos Personales', {
            'fields': ('nombres', 'apellidos', 'dni', 'fecha_nacimiento', 'genero')
        }),
        ('Contacto', {
            'fields': ('telefono', 'email', 'direccion')
        }),
        ('Información Clínica', {
            'fields': ('especialidad_requerida', 'activo', 'fecha_registro')
        }),
    )