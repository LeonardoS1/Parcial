from django.urls import URLPattern, path
from rest_fundacion.views import lista_fundacion, detalle_fundacion
from rest_fundacion.viewsLogin import login
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns = [
    path('lista_fundacion', lista_fundacion, name= "lista_fundacion"),
    path('detalle_fundaciones/<id>', detalle_fundacion, name="detalle_fundacion"),
    path('login', login, name="login"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)