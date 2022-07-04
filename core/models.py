from pickle import TRUE
import django
from django.db import models

# Create your models here.
#modelo para contacto
opciones_consulta = [
    [0,'bandana'],
    [1, 'correa'],
    [2, 'identificacion']
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de Contacto")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos de Contacto")
    email = models.EmailField(max_length=50, verbose_name="Email de Contacto")
    direccion =models.CharField(max_length=60, verbose_name="dirección de Contacto")
    telefono =models.CharField(max_length=9, verbose_name="teléfono de Contacto")
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=TRUE)
    nombre = models.CharField(max_length=50, verbose_name="Nombre del Producto")
    color = models.CharField(max_length=50, verbose_name="Color de Producto")
    precio = models.IntegerField(verbose_name="Precio del Producto")
    tipo = models.IntegerField(choices=opciones_consulta)
    imagen =models.ImageField(upload_to = "imagenes/", verbose_name="Imágen del Producto")
    def __str__(self):
      return self.nombre

class Fundacion(models.Model):
    id = models.AutoField(primary_key=TRUE)
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Fundacion")
    descripcion = models.CharField(max_length=800, verbose_name="Descripcion de la Fundacion")
    imagen =models.ImageField(upload_to = "fundaciones/", verbose_name="Imágen de la Fundacion")
    def __str__(self):
        return self.nombre
  #tablas  

 