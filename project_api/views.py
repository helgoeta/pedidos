from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Cliente, Produto, Pedido
from .serializers import ClienteSerializer, ProdutoSerializer, PedidoSerializer, HelloSerializer


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
            'Pão com maionese',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

# CLIENTES
@api_view(['GET'])
def view_clientes(request):

    #checking for the parameters from the URL
    clientes= Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    if clientes:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_cliente(request):
    cliente = ClienteSerializer(data=request.data)

    # validating for already existing data
    if Cliente.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Esse cliente já existe')

    if cliente.is_valid():
        cliente.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_clientes(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    data = ClienteSerializer(instance=cliente, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#PRODUTOS
@api_view(['GET'])
def view_produtos(request):

    #checking for the parameters from the URL
    produtos= Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    if produtos:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_produto(request):
    produto = ProdutoSerializer(data=request.data)

    # validating for already existing data
    if Produto.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Esse produto já existe')

    if produto.is_valid():
        produto.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    data = ProdutoSerializer(instance=produto, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#PEDIDOS
@api_view(['GET'])
def view_pedidos(request):

    #checking for the parameters from the URL
    pedidos= Pedido.objects.all()
    serializer = PedidoSerializer(pedidos, many=True)
    if pedidos:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_pedido(request):
    pedido = PedidoSerializer(data=request.data)

    if pedido.is_valid():
        pedido.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_pedido(request, pk):
    pedido = Pedido.objects.get(pk=pk)
    data = PedidoSerializer(instance=pedido, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
