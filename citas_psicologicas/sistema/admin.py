from django.contrib import admin
from .models import ClinicaConfig, Especialidad

@admin.register(ClinicaConfig)
class ClinicaConfigAdmin(admin.ModelAdmin):
    # Esto evita que creen múltiples configuraciones (solo debe haber una)
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True
    
    list_display = ('nombre_institucion', 'telefono_contacto', 'email_contacto')

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)