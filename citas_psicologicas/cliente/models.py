from django.db import models
from sistema.models import Especialidad


class Cliente(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    dni = models.CharField(max_length=15, unique=True, verbose_name="DNI / Documento")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, verbose_name="Género")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(blank=True, verbose_name="Correo Electrónico")
    direccion = models.TextField(blank=True, verbose_name="Dirección")
    especialidad_requerida = models.ForeignKey(
        Especialidad,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Especialidad Requerida",
    )
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")
    activo = models.BooleanField(default=True, verbose_name="Cliente Activo")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f"{self.apellidos}, {self.nombres} ({self.dni})"