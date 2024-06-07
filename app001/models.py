from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Escuela(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    cue = models.IntegerField(blank=True)
    cuise = models.IntegerField()
    direccion = models.CharField(max_length=200, blank=True)
    localidad = models.CharField(max_length=200, blank=True)
    departamento = models.CharField(max_length=200, blank=True)
    referente = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True)
    detalle = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cuise} - {self.nombre}"


class Directivo(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    escuela = models.ForeignKey(
        Escuela, on_delete=models.DO_NOTHING, blank=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Netbook(models.Model):
    identificador = models.IntegerField(blank=True)
    serie = models.CharField(max_length=50, blank=True)
    marca = models.CharField(max_length=50, blank=True)
    modelo = models.CharField(max_length=50, blank=True)
    imagen_win = models.CharField(max_length=50, blank=True)    
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, blank=True)
    estado_pila_choices = (
        ('ok', 'ok'),
        ('agotada', 'agotada'),
        ('cambiada', 'cambiada')
    )
    estado_pila = models.CharField(max_length=20,
                                   choices=estado_pila_choices, default='agotada')
    arranques = models.IntegerField(blank=True, default=0)
    fecha_expiracion = models.DateField(blank=True, null=True)
    sn = models.CharField(max_length=30, blank=True)
    hid = models.CharField(max_length=20, blank=True)
    boottick = models.CharField(max_length=10, blank=True)
    estado_disco_choices = (
        ('llevado', 'llevado'),
        ('flasheado', 'flasheado'),
        ('sin flashear', 'sin flashear')
    )
    estado_disco = models.CharField(max_length=20,
                                    choices=estado_disco_choices, default='sin flashear')

    Estado_CHOICES = (
        ('ok', 'ok'),
        ('no funciona', 'no funciona'),
        ('bloqueada', 'bloqueada'),
        ('pendiente de revision', 'pendiente de revision'),
        ('pendiente migracion', 'pendiente migracion'),
        ('robada', 'robada')
    )
    estado = models.CharField(
        max_length=30, choices=Estado_CHOICES, default="pendiente de revision")
    detalle = models.TextField(blank=True)
    imagen1 = models.ImageField(upload_to='netbooks', blank=True)

    def __str__(self):
        return f"{self.marca} - {self.serie}"


class Actividad(models.Model):
    fecha = models.DateTimeField()
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tipo_actividad_choices = (
        ('creacion', 'creación'),
        ('consulta', 'consulta'),
        ('modificacion', 'modificación'),
        ('eliminacion', 'eliminación')
    )
    tipo_actividad = models.CharField(
        max_length=100, choices=tipo_actividad_choices)
    entidad = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.fecha} - {self.autor} - {self.tipo_actividad} - {self.entidad}"


class Informe(models.Model):
    fecha = models.DateTimeField()
    detalle = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    estado = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.autor} - {self.fecha}"
