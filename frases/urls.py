from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frases.views.home', name='home'),
    
    url(r'^', include('frases_app.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
