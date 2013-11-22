from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Author
from serializers import AuthorSerializer

@api_view(['GET', 'POST'])
def author_list(request, format=None):
    """
    Listado de todos los autores, o crear un nuevo autor
    """
    
    # En solicitudes GET devolvemos el JSON con el listado de autores
    if request.method == 'GET':
        authors    = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    # En solicitudes POST insertamos los datos del autor
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk, format=None):
    """
    Obtener, actualizar o eliminar un autor
    """

    # Obtener el autor con el que se va a trabajar
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Devolver los datos del autor
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Actualizar los datos del autor
        serializer = AuthorSerializer(author, data=request.DATA)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Eliminar un autor
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
