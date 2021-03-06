from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import TxcTitulo
from app.serializables import TxcTituloS


@api_view(['GET', 'POST'])
def lista_objetos(request):
    """
    Lista de todos los titulos, o crear un  nuevo
    """
    if request.method == 'GET':
        objeto = TxcTitulo.objects.all()
        serializador = TxcTituloS(objeto, many=True)
        return Response(serializador.data)

    elif request.method == 'POST':
        serializador = TxcTituloS(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data,status=status.HTTP_201_CREATED)
            return Response(serializador.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT','DELETE'])
def detalle_objetos(request, pk):
    """
    Actualiza, elimina un objeto segun su id
    """
    try:
        objeto = TxcTitulo.objects.get(pk=pk)
    except objeto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = TxcTituloS(objeto)
        return Response(serializador.data)

    elif request.method == 'PUT':
        serializador = TxcTituloS(objeto, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        objeto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
