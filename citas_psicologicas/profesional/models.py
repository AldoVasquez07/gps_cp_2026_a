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
