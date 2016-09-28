from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import TxdHorariodetalle
from app.serializables import TxdHorariodetalleS


@api_view(['GET', 'POST'])
def lista_objetos(request):
    """
    Lista de todos los Horariodetalles, o crea uno nuevo.
    """
    if request.method == 'GET':
        objeto = TxdHorariodetalle.objects.all()
        serializador = TxdHorariodetalleS(objeto, many=True)
        return Response(serializador.data)

    elif request.method == 'POST':
        serializador = TxdHorariodetalleS(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_objetos(request, pk):
    """
    Actuliza, elimina un objeto segun su id
    """
    try:
        objeto = TxdHorariodetalle.objects.get(pk=pk)
    except objeto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = TxdHorariodetalleS(objeto)
        return Response(serializador.data)

    elif request.method == 'PUT':
        serializador = TxdHorariodetalleS(objeto, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        objeto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
