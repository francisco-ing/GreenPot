from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class TipoEnvio(models.Model):
    id_tp_envio = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=200) 

    def __str__(self) :
        return str(self.id_tp_envio)+" "+self.nombre

class Envio(models.Model):
    id_envio = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=200)
    tipo_envio =models.ForeignKey(to=TipoEnvio, on_delete=models.CASCADE)

    def __str__(self) :
        return str(self.id_envio)+" "+self.direccion+" "+str(self.tipo_envio)

class ImagenesProductos(models.Model):
    codigo = models.CharField(max_length=4,primary_key=True)
    detalle = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)

    def __str__(self):
        return self.detalle +" ("+ self.codigo +")"


class Producto(models.Model):
    codigo = models.CharField(max_length=4,primary_key=True)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    imagen = models.CharField(max_length=200)
    tipo = models.IntegerField(default=1)

    def tachado(self):
        if self.oferta:
            return "$"+str(round(self.precio*1.2))
        return ""

    def __str__(self):
        return self.detalle +" ("+ self.codigo +")"\

class Venta(models.Model):
    id  = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    envio = models.ForeignKey(to=Envio, on_delete=models.CASCADE, default=0)

    def __str__(self) :
        return str(self.id)+" "+self.cliente.username+" "+str(self.fecha)[0:16]
    
class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self) :
        return str(self.id)+" "+self.producto.detalle[0:20]+" "+str(self.venta.id)