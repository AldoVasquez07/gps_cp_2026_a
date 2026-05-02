from django.db import models

class ClinicaConfig(models.Model):
    """Configuración global de la clínica o consultorio"""
    nombre_institucion = models.CharField(max_length=150, verbose_name="Nombre de la Institución")
    telefono_contacto = models.CharField(max_length=20, verbose_name="Teléfono de Contacto")
    email_contacto = models.EmailField(verbose_name="Correo Electrónico")
    direccion = models.TextField(verbose_name="Dirección Física")
    horario_atencion = models.CharField(max_length=100, help_text="Ej: Lun-Vie 08:00 - 18:00")

    class Meta:
        verbose_name = "Configuración del Sistema"
        verbose_name_plural = "Configuración del Sistema"

    def __str__(self):
        return self.nombre_institucion

class Especialidad(models.Model):
    """Catálogo de especialidades psicológicas"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.nombre