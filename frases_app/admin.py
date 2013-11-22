from django.contrib import admin

from models import Author
from models import Category
from models import Sentence

class AdminAuthor(admin.ModelAdmin):
    list_display = ['name', 'count_sentences']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'count_sentences']


class AdminSentence(admin.ModelAdmin):
    list_display = [
        'author',     
        'category',   
        'text',       
        'public',     
        'date',       
        'insert_date',
        'votes',      
    ]

admin.site.register(Author, AdminAuthor)
admin.site.register(Category, AdminCategory)
admin.site.register(Sentence, AdminSentence)
