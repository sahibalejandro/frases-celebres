from models import Author
from models import Sentence
from serializers import AuthorSerializer
from serializers import SentenceSerializer

from rest_framework import viewsets
from rest_framework import permissions


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Listado y detalle de los autores
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class SentenceViewSet(viewsets.ModelViewSet):
    """
    Lectura y escritura de frases celebres
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
