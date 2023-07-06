from django.shortcuts import render, redirect
from  .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.db.models import F
from django.contrib import messages
import requests

def suscribir(request):
    context = {} 
    if request.method == "POST":
        if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            context["mensaje"] = resp.json()["mensaje"]
            suscrito(request, context)
            return render(request, 'core/fundacion.html', context)
    else:
        suscrito(request, context)
        return render(request, 'core/fundacion.html', context)

def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"] 

def carrito(request):
    context = {"carro":request.session.get("carro", [])}
    suscrito(request, context)
    return render(request, 'core/carrito.html',  context)

def home(request):
    return render(request, 'core/principal.html')

def login(request):
    return render(request, 'core/login.html')

def logout(request):
    return logout_then_login(request, login_url="home")

def fundacion(request):
    return render(request, 'core/fundacion.html')

def colaboradores(request):
    return render(request, 'core/colaboradores.html')

def micuenta(request):
    ventas = Venta.objects.filter(cliente = request.user)
    return render(request, 'core/micuenta.html', {'ventas':ventas})

def seguimiento(request):
    ventas = Venta.objects.filter(cliente = request.user)
    return render(request, 'core/seguimiento.html', {'ventas':ventas})

def productos(request):
    plantas = ImagenesProductos.objects.all()
    return render(request, 'core/productos.html',{'plantas':plantas})

def arbustos(request):
    productos = Producto.objects.all()
    return render(request, 'core/Aarbustos.html',{'productos':productos})

def flores(request):
    productos = Producto.objects.all()
    return render(request, 'core/Aflores.html',{'productos':productos})

def herramientas(request):
    productos = Producto.objects.all()
    return render(request, 'core/Aherramientas.html',{'productos':productos})

def maceteros(request):
    productos = Producto.objects.all()
    return render(request, 'core/Amaceteros.html',{'productos':productos})

def ofertas(request):
    productos = Producto.objects.all()
    return render(request, 'core/Aofertas.html',{'productos':productos})

def tierra(request):
    productos = Producto.objects.all()
    return render(request, 'core/Atierra.html',{'productos':productos})

def detalleVentas(request, detalleventa):
    detalle = DetalleVenta.objects.filter(venta = detalleventa)
    return render(request, 'core/detalleVentas.html',{'detalle':detalle})

def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
        # DESCUENTA STOCK
        Producto.objects.filter(codigo=item[0]).update(stock=F('stock') - item[4])
    venta = Venta()
    envio = Envio()
    envio.direccion = 'Melipilla 6669'
    envio.tipo_envio = TipoEnvio.objects.all().first()
    venta.cliente = request.user
    context = {}
    suscrito(request, context)
    if context['suscrito'] == True:
        venta.total = total * 0.95
    else:
        venta.total = total
    venta.envio = envio
    envio.save()
    venta.save()
    for item in carro:
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(codigo = item[0])
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()
        request.session["carro"] = []
    return redirect(to="carrito")

def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carrito")

def addtocar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo and producto.stock > item[4]:
            item[4] += 1
            item[5] = item[3] * item[4]
            print('1')
            break
        elif item[0] == codigo and producto.stock <= item[4]:
             if producto.tipo == 1:
                return redirect(to="herramientas")
             elif producto.tipo == 2:
                return redirect(to="flores")
             elif producto.tipo == 3:
                return redirect(to="maceteros")
             elif producto.tipo == 4:
                return redirect(to="arbustos")
             elif producto.tipo == 5:
                return redirect(to="tierra")
    else:
        carro.append([codigo, producto.detalle, producto.imagen, producto.precio, 1, producto.precio])
        print('2')
    request.session["carro"] = carro
    if producto.tipo == 1:
        return redirect(to="herramientas")
    elif producto.tipo == 2:
        return redirect(to="flores")
    elif producto.tipo == 3:
        return redirect(to="maceteros")
    elif producto.tipo == 4:
        return redirect(to="arbustos")
    elif producto.tipo == 5:
        return redirect(to="tierra")
    
def addtocarofertas(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo and producto.stock > item[4]:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
        else:
            print("no hay stock")
            break
    else:
        carro.append([codigo, producto.detalle, producto.imagen, producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="ofertas")

def limpiar(request):
    request.session.flush()
    return redirect(to="flores")

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'core/registro.html', {'form':registro})