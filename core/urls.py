from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',home, name="home"),
    path('logout',logout, name="logout"),
    path('login',LoginView.as_view(template_name='core/login.html'), name="login"),
    path('productos',productos, name="productos"),
    path('micuenta',micuenta, name="micuenta"),
    path('Aarbustos',arbustos, name="arbustos"),
    path('Aflores',flores, name="flores"),
    path('Aherramientas',herramientas, name="herramientas"),
    path('Amaceteros',maceteros, name="maceteros"),
    path('Aofertas',ofertas, name="ofertas"),
    path('Atierra',tierra, name="tierra"),
    path('carrito', carrito, name="carrito"),
    path('addtocar/<codigo>', addtocar, name="addtocar"),
    path('addtocarofertas/<codigo>', addtocarofertas, name="addtocarofertas"),
    path('dropitem/<codigo>', dropitem, name="dropitem"),
    path('comprar', comprar, name="comprar"),
    path('registro', registro, name="registro"),
    path('limpiar', limpiar, name="limpiar"),
    path('seguimiento', seguimiento, name="seguimiento"),
    path('colaboradores', colaboradores, name="colaboradores"),
    path('detalleVentas/<detalleventa>', detalleVentas, name="detalleVentas"),
    path('suscribir', suscribir, name="suscribir"),
]
