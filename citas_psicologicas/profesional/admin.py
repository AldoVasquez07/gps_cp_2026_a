from django.contrib import admin
from .models import Profesional, HorarioDisponible


class HorarioDisponibleInline(admin.TabularInline):
    """Permite gestionar los horarios del profesional dentro de su ficha"""
    model = HorarioDisponible
    extra = 1
    fields = ('dia_semana', 'hora_inicio', 'hora_fin', 'activo')
 
 
@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = (
        'apellidos', 'nombres', 'codigo_colegiatura',
        'telefono', 'email', 'modalidad_atencion',
        'anos_experiencia', 'activo',
    )
    list_filter = ('activo', 'genero', 'modalidad_atencion', 'especialidades')
    search_fields = ('nombres', 'apellidos', 'dni', 'email', 'codigo_colegiatura')
    ordering = ('apellidos', 'nombres')
    list_editable = ('activo',)
    readonly_fields = ('fecha_registro',)
    filter_horizontal = ('especialidades',)
    inlines = [HorarioDisponibleInline]
 
    fieldsets = (
        ('Datos Personales', {
            'fields': ('nombres', 'apellidos', 'dni', 'fecha_nacimiento', 'genero'),
        }),
        ('Contacto', {
            'fields': ('telefono', 'email'),
        }),
        ('Datos Profesionales', {
            'fields': (
                'codigo_colegiatura', 'especialidades',
                'anos_experiencia', 'modalidad_atencion',
            ),
        }),
        ('Configuración de Citas', {
            'fields': ('duracion_cita_minutos', 'tarifa_sesion'),
        }),
        ('Estado', {
            'fields': ('activo', 'fecha_registro'),
        }),
    )
 
 
@admin.register(HorarioDisponible)
class HorarioDisponibleAdmin(admin.ModelAdmin):
    list_display = (
        'profesional', 'dia_semana', 'hora_inicio', 'hora_fin', 'activo',
    )
    list_filter = ('activo', 'dia_semana', 'profesional')
    search_fields = ('profesional__nombres', 'profesional__apellidos')
    ordering = ('profesional', 'dia_semana', 'hora_inicio')
    list_editable = ('activo',)