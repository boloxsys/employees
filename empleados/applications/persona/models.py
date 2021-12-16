from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
    def __str__(self):
        return str(self.id) + '-' + self.habilidad
# Create your models here.
class Empleado(models.Model):
    """ Modelo Para tabla Empleado"""

    job_choices = (
        ('0', 'Contable'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=1, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name