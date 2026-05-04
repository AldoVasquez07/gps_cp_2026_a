from django.db import models
from sistema.models import Especialidad

class Profesional(models.Model):
    """Psicólogo o profesional de salud mental registrado en el sistema"""
 
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
 
    MODALIDAD_CHOICES = [
        ('PRESENCIAL', 'Presencial'),
        ('VIRTUAL',    'Virtual'),
        ('AMBAS',      'Presencial y Virtual'),
    ]

    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    dni = models.CharField(max_length=15, unique=True, verbose_name="DNI / Documento")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, verbose_name="Género")

    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    