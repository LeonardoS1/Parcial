from rest_framework import serializers
from core.models import Fundacion
        
class FundacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundacion
        fields = ['id', 'nombre','descripcion','imagen']