from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    apellido_P = models.CharField(max_length=100)
    apellido_M = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    email = models.EmailField()
    celular = models.PositiveIntegerField()
    genero = models.CharField(max_length=100)
    pedido = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


