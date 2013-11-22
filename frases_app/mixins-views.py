from models import Author
from serializers import AuthorSerializer

from rest_framework import mixins
from rest_framework import generics


class AuthorList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    """
    Listado de todos los autores, o crear un nuevo autor
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AuthorDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    """
    Obtener, actualizar o eliminar un autor
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        # Devolver los datos del autor
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        # Actualizar al autor
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        # Eliminar al autor
        return self.destroy(request, *args, **kwargs)
