from django.contrib import admin
from django.urls import path, include  
from core import views
from django.conf.urls.static import static
from django.conf import settings           

urlpatterns = [
    path('', views.paginaPrincipal, name="PaginaPrincipal"),
    path('admin/', admin.site.urls),
    path('contacto/', views.agregar_Contacto, name="contacto"),
    path('productos/<int:tipo>/', views.productos, name="productos"),
    path('agregar_Producto/', views.agregar_Producto, name="agregar_Producto"),
    path('eliminar_Producto/<int:id>/', views.eliminar_Producto, name="eliminar_Producto"),
    path('editar_Producto/<int:id>/', views.editar_Producto, name='editar_Producto'),
    path('donaciones/', views.fundaciones, name="donaciones"),
    path('Fundacion/<int:id>/', views.fundacion, name="Fundacion"),
    path('editar_Fundacion/<int:id>/', views.editar_Fundacion, name="editar_Fundacion"),
    path('agregar_Fundacion/', views.agregar_Fundacion, name="agregar_Fundacion"),
    path('eliminar_Fundacion/<int:id>/', views.eliminar_Fundacion, name="eliminar_Fundacion"),
    path('eliminar_Contacto/<int:id>/', views.eliminar_Contacto, name="eliminar_Contacto"),
    path('editar_Contacto/<int:id>/', views.editar_Contacto, name="editar_Contacto"),
    path('contactos/', views.contactos, name="contactos"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('tienda/', views.tienda, name="tienda"),
    path('api/', include('rest_fundacion.urls')),
    path('cerrar_sesion',views.cerrar_sesion,name="cerrar_sesion"),
    path('login/',views.login,name="login"),
    path('crear_usuario',views.crear_usuario,name="crear_usuario"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
