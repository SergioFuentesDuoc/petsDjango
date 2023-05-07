from django.db import models

# Create your models here.
class Cliente(models.Model):
        codigoCliente = models.AutoField(primary_key=True)
        nombreCliente = models.CharField(max_length=30)
        telefonoCliente = models.IntegerField()
        correoCliente = models.CharField(max_length=50)
        passCliente = models.CharField(max_length=30)


        def __str__(self):
                return self.nombreCliente

class Mascota(models.Model):
        codigoChip = models.IntegerField()
        nombreMascota = models.CharField(max_length=50)
        nombreCliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

        def __str__(self):
                return self.nombreMascota


class Producto(models.Model):
        nombreProducto = models.CharField(max_length=50)
        precioProducto = models.IntegerField()
        descripcionProducto = models.TextField()
        
        def __str__(self):
                return self.nombreProducto
                
