#-*- coding:utf-8 -*-
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def __unicode__(self):
        return self.name

    def count_sentences(self):
        return self.sentence_set.count()


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __unicode__(self):
        return self.name

    def count_sentences(self):
        return self.sentence_set.count()


class Sentence(models.Model):
    author      = models.ForeignKey(Author)
    category    = models.ForeignKey(Category)
    text        = models.CharField(max_length=500)
    public      = models.BooleanField(default=False)
    date        = models.DateField()
    insert_date = models.DateTimeField(auto_now_add=True)
    votes       = models.IntegerField(default=0)

    class Meta:
        ordering = ['-insert_date']
        verbose_name = 'frase celebre'
        verbose_name_plural = 'frases celebres'

    def __unicode__(self):
        return self.text
