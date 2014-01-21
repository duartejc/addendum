from django.conf.urls import patterns, url
from calendario import views

urlpatterns = patterns('', 
    url(r'^$', views.main, name='main'),
    url(r'^ajax/eventos/', views.json_get_events, name='listar_eventos'),
)