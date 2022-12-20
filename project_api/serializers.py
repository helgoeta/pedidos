from rest_framework import serializers
from .models import Cliente, Produto


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=50)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'data_de_cadastro', 'ultima_alteracao')


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'nome', 'codigo', 'tabela_preco', 'multiplo', 'data_cadastro', 'ultima_alteracao')
