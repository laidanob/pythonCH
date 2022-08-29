from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=999)
    precio = models.IntegerField()
    fecha = models.CharField(max_length=999)
