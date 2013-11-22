from django.forms import widgets
from rest_framework import serializers
from models import Author
from models import Sentence


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Author
        fields = ('id', 'name')


class SentenceSerializer(serializers.ModelSerializer):

    # Crear algunos fields extra para tener una mejor descripcion
    # Usar serializers.Field (untyped field) para que los campos sean de
    # solo lectura, de esta manera no se usan estos campos para actualizar
    # instancias de modelos cuando este objeto es deserializado
    author_name   = serializers.Field(source='author.name')
    category_name = serializers.Field(source='category.name')
    
    class Meta:
        model = Sentence
        fields = (
            'id',
            'author',
            'author_name',
            'category',
            'category_name',
            'text',
            'public',
            'date',
            'insert_date',
            'votes',
        )
