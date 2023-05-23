from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Experiencia(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Puesto")
    empresa = models.CharField(max_length=50, verbose_name="Nombre Empresa")
    descripcion = RichTextField(verbose_name="Descripción")
    fecha_desde = models.DateField(verbose_name="Fecha de inicio")
    fecha_hasta = models.DateField(verbose_name="Fecha de fin", null=True, blank=True)
    ubicacion = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ["fecha_desde"]

    def __str__(self):
        return self.titulo
