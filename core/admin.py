from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Producto)
admin.site.register(ImagenesProductos)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Envio)
admin.site.register(TipoEnvio)