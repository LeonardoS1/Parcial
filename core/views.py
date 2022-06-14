from importlib.metadata import files
from django.urls import reverse
from django.shortcuts import render, redirect
from core.forms import ContactoForm, ProductoForm, FundacionForm
from core.models import Contacto, Fundacion, Producto
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def paginaPrincipal(request):
    return render(request, "core/PaginaPrincipal.html")

def nosotros(request):
    return render(request, "core/Nosotros.html")

def tienda(request):
    return render(request, "core/Tienda.html")


#crud producto 
def productos(request, tipo):
    productos = Producto.objects.all().filter(tipo = tipo)
    
    datos = {
        'productos': productos
        }
    return render(request, "core/Productos.html", datos)
 
def agregar_Producto(request):
    
    datos = {
        'agregar_Producto': ProductoForm
    }
    
    if request.method == 'POST':
        formulario =ProductoForm(request.POST, files=request.FILES)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
        else:
            datos['mensaje'] = 'error'
            
    return render(request, 'core/agregar_Producto.html', datos)

def editar_Producto(request, id):
    producto = Producto.objects.get(id = id)
    
    datos = {
        'form': ProductoForm(instance = producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(instance = producto, data=request.POST, files=request.FILES)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Editado Correctamente'
        datos["form"] = formulario
            
    return render(request, 'core/editar_Producto.html', datos)

def eliminar_Producto(request, id):
    producto = Producto.objects.get(id = id)
    c = producto.tipo
   
    producto.delete()
    
    return redirect("productos" , c)



#crud fundaciones 
def fundaciones(request):
    fundaciones = Fundacion.objects.all()
    
    datos = {
        'fundaciones': fundaciones
        }
    return render(request, "core/donaciones.html", datos)
 
def fundacion(request, id):
    fundacion = Fundacion.objects.get(id = id)
    
    datos = {
        'fundacion': fundacion
        }
    return render(request, "core/Fundacion.html", datos)

def agregar_Fundacion(request):
    
    datos = {
        'agregar_Fundacion': FundacionForm
    }
    
    if request.method == 'POST':
        formulario =FundacionForm(request.POST, files=request.FILES)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
        else:
            datos['mensaje'] = 'error'
            
    return render(request, 'core/agregar_Fundacion.html', datos)

def editar_Fundacion(request, id):
    fundacion = Fundacion.objects.get(id = id)
    
    datos = {
        'editar_Fundacion': FundacionForm(instance = fundacion)
    }
    
    if request.method == 'POST':
        formulario = FundacionForm(instance = fundacion, data=request.POST, files=request.FILES)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Editado Correctamente'
        datos["editar_Fundacion"] = formulario
            
    return render(request, 'core/editar_Fundacion.html', datos)

def eliminar_Fundacion(request, id):
    fundacion = Fundacion.objects.get(id = id)
    fundacion.delete()
    return HttpResponseRedirect(reverse('donaciones'))





#crud contacto 
def contactos(request):
    contacto = Contacto.objects.all
    
    datos = {
        'contactos': contacto
    }
    
    return render(request, 'core/Contactos.html', datos)
 
def agregar_Contacto(request):
    datos = {
        'agregar_Contacto': ContactoForm
    }
    
    if request.method == 'POST':
        formulario =ContactoForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
            
    return render(request, 'core/Contacto.html', datos)

def editar_Contacto(request, id):
    contacto = Contacto.objects.get(id = id)
    
    datos = {
        'editar_Contacto': ContactoForm(instance = contacto)
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(instance = contacto, data=request.POST, files=request.FILES)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Editado Correctamente'
        datos["editar_Contacto"] = formulario
            
    return render(request, 'core/editar_Contacto.html', datos)

def eliminar_Contacto(request, id):
    contacto = Contacto.objects.get(id = id)
    
    contacto.delete()
    
    return HttpResponseRedirect(reverse('contactos'))



