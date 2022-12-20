from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Cliente
from .serializers import ClienteSerializer, HelloSerializer


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