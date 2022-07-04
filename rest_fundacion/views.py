from django.shortcuts import render
from ast import Return
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
#from rest_fundacion.models import Fundacion
from core.views import fundacion
from .serializers import FundacionSerializer
#autentificaciones
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Fundacion
# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_fundacion(request):
    if request.method=='GET':
        fundacion = Fundacion.objects.all()
        serializer = FundacionSerializer(fundacion, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FundacionSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE']) 
def detalle_fundacion(request, id):
    try:
        producto= Fundacion.objects.get(id=id)
    except Fundacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FundacionSerializer(fundacion)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FundacionSerializer(fundacion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated,))      
#def suscribirse(request, id):