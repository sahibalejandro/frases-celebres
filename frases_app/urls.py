from django.conf.urls import patterns, url, include
from frases_app import rest_views
from rest_framework.routers import DefaultRouter

# Crear el router y registrar las viewsets de REST
router = DefaultRouter()
router.register(r'authors', rest_views.AuthorViewSet)
router.register(r'sentences', rest_views.SentenceViewSet)

urlpatterns = patterns('',
    url(r'^rest/', include(router.urls)),
)
