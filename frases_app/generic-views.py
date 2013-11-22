from models import Author
from models import Sentence
from serializers import AuthorSerializer
from serializers import SentenceSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import permissions

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'authors': reverse('authors-list', request=request, format=format),
        'sentences': reverse('sentences-list', request=request, format=format),
    })

class AuthorList(generics.ListAPIView):
    """
    Listado de todos los autores, o crear un nuevo autor
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    """
    Obtener, actualizar o eliminar un autor
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SentenceList(generics.ListAPIView):
    """
    Listado de frases celebres
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


class SentenceDetail(generics.RetrieveAPIView):
    """
    Detalle de frase celebre
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
