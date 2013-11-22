from models import Author
from serializers import AuthorSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AuthorList(APIView):
    """
    Listado de todos los autores, o crear un nuevo autor
    """
    
    # En solicitudes GET devolvemos el JSON con el listado de autores
    def get(self, request, format=None):
        authors    = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    # En solicitudes POST insertamos los datos del autor
    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):
    """
    Obtener, actualizar o eliminar un autor
    """

    # Obtener el autor con el que se va a trabajar
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # Devolver los datos del autor
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        # Actualizar los datos del autor
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.DATA)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        # Eliminar un autor
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
