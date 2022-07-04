from importlib.metadata import files
from django.urls import reverse
from django.shortcuts import render, redirect
from core.forms import ContactoForm, ProductoForm, FundacionForm
from core.models import Contacto, Fundacion, Producto
from django.http import HttpResponse, HttpResponseRedirect
import requests
#cosas que se deben importar para el login
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login

#decorador para hacer que la vista sea obligatoria
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


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
 
@staff_member_required(login_url = 'PaginaPrincipal')
@login_required(login_url = "login")
def agregar_Producto(request):
    
    datos = {
        'agregar_Producto': ProductoForm
    }
    
    if request.method == 'POST':
         #files para imagenes
        formulario =ProductoForm(request.POST, files=request.FILES)
        print(formulario)
       
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
        else:
            datos['mensaje'] = 'error'
            
    return render(request, 'core/agregar_Producto.html', datos)

@staff_member_required(login_url = 'PaginaPrincipal')
@login_required(login_url = "login")
def editar_Producto(request, id):
    #trae el objeto con su id
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

@staff_member_required(login_url = 'PaginaPrincipal')
@login_required(login_url = "login")
def eliminar_Producto(request, id):
    producto = Producto.objects.get(id = id)
    c = producto.tipo
   
    producto.delete()
    
    # redirect me lo redirecciona no me deja volver atras(repetir la solicitud) redirecciono a el metodo productos que esta en el viws
    return redirect("productos" , c)



#crud fundaciones 
def fundaciones(request):
    fundaciones = Fundacion.objects.all()
    
    datos = {
        'fundaciones': fundaciones
        }
    return render(request, "core/donaciones.html", datos)
    
#quinta funcion que trae una sola fundacion
def fundacion(request, id):
    fundacion = Fundacion.objects.get(id = id)
    
    datos = {
        'fundacion': fundacion
        }
    return render(request, "core/Fundacion.html", datos)

@staff_member_required(login_url = 'PaginaPrincipal')
@login_required(login_url = "login")
def agregar_Fundacion(request):
    
    datos = {
        'agregar_Fundacion': FundacionForm
    }
    
    
    if request.method == 'POST':
        formulario =FundacionForm(request.POST, files=request.FILES)
        
        if formulario.is_valid:
            requests.post('http://127.0.0.1:8000/api/lista_fundacion', formulario)
            datos['mensaje'] = 'Guardado Correctamente'
        else:
            datos['mensaje'] = 'error'
            
    return render(request, 'core/agregar_Fundacion.html', datos)

@staff_member_required(login_url = 'PaginaPrincipal')
@login_required(login_url = "login")
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

@staff_member_required(login_url = 'PaginaPrincipal')
@login_required(login_url = "login")
def eliminar_Fundacion(request, id):
    fundacion = Fundacion.objects.get(id = id)
    fundacion.delete()
    return HttpResponseRedirect(reverse('donaciones'))





#crud contacto 
@staff_member_required(login_url = 'PaginaPrincipal')
@login_required(login_url = "login")
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


@login_required(login_url = "login")
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

@login_required(login_url = "login")
def eliminar_Contacto(request, id):
    contacto = Contacto.objects.get(id = id)
    
    contacto.delete()
    
    return HttpResponseRedirect(reverse('contactos'))

def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('PaginaPrincipal'))

#para logear al usuario
def login(request):
    if request.POST:
        usuario = request.POST.get('usuario','')
        contrasenia = request.POST.get('contrasenia','')
        user = authenticate(request,username=usuario, password = contrasenia)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('PaginaPrincipal'))
    return render(request,'core/login.html')
    
@staff_member_required(login_url = 'index')
@login_required(login_url = 'login')
def crear_usuario(request):
    if request.POST:
        first_name= request.POST.get('first_name',False)
        last_name= request.POST.get('last_name',False)
        email= request.POST.get('email',False)
        username= request.POST.get('username',False)
        password= request.POST.get('password',False)
        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return HttpResponseRedirect(reverse('PaginaPrincipal'))
    return render(request,'core/crear_usuario.html')

