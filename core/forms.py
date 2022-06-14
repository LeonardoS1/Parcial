from msilib.schema import AppId
from django import forms
from django.forms import ModelForm
from .models import Contacto, Producto, Fundacion


class ContactoForm(ModelForm):
    
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellidos', 'email', 'direccion', 'telefono', 'nombre']

class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre', 'color', 'precio', 'tipo', "imagen"]

class FundacionForm(ModelForm):
    
    class Meta:
        model = Fundacion
        fields = ['nombre', 'descripcion', "imagen"]
  
