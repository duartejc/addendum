from django.conf.urls import patterns, url

from common import views

urlpatterns = patterns('', 
    url(r'^buscar/$', views.search, name='buscar'),
)