from rest_framework import serializers
from .models import Cliente


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=50)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'data_de_cadastro', 'ultima_alteracao')
