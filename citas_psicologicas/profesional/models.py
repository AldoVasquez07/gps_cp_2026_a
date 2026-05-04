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

    codigo_colegiatura = models.CharField(
        max_Length=30,
        unique=True,
        verbose_name="N° de Colegiatura",
        help_text="Número de registro en el Colegio de Psicólogos",
    )

    especialidades = models.ManyToManyField(
        Especialidad,
        blank=True,
        verbose_name="Especialidades",
        related_name="profesionales",
    )
    anos_experiencia = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Años de Experiencia",
    )
    modalidad_atencion = models.CharField(
        max_length=10,
        choices=MODALIDAD_CHOICES,
        default='PRESENCIAL',
        verbose_name="Modalidad de Atención",
    )

    duracion_cita_minutos = models.PositiveSmallIntegerField(
        default=60,
        verbose_name="Duración de Cita (min)",
        help_text="Duración estándar de cada sesión en minutos",
    )
    tarifa_sesion = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Tarifa por Sesión (S/)",
    )

    activo = models.BooleanField(default=True, verbose_name="Profesional Activo")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")
 
    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
        ordering = ['apellidos', 'nombres']
 
    def __str__(self):
        return f"{self.apellidos}, {self.nombres} — Colegiatura: {self.codigo_colegiatura}"
 
    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"
    
class HorarioDisponible(models.Model):
    """Franjas horarias semanales en que un profesional atiende citas"""
 
    DIA_CHOICES = [
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ]
 
    profesional = models.ForeignKey(
        Profesional,
        on_delete=models.CASCADE,
        related_name='horarios',
        verbose_name="Profesional",
    )
    dia_semana = models.PositiveSmallIntegerField(choices=DIA_CHOICES, verbose_name="Día de la Semana")
    hora_inicio = models.TimeField(verbose_name="Hora de Inicio")
    hora_fin = models.TimeField(verbose_name="Hora de Fin")
    activo = models.BooleanField(default=True, verbose_name="Activo")
 
    class Meta:
        verbose_name = "Horario Disponible"
        verbose_name_plural = "Horarios Disponibles"
        ordering = ['profesional', 'dia_semana', 'hora_inicio']
        unique_together = ('profesional', 'dia_semana', 'hora_inicio')
 
    def __str__(self):
        return (
            f"{self.profesional.nombre_completo} — "
            f"{self.get_dia_semana_display()} "
            f"{self.hora_inicio.strftime('%H:%M')} a {self.hora_fin.strftime('%H:%M')}"
        )