from django.conf.urls import patterns, url

from pessoas import views

urlpatterns = patterns('', 
    url(r'^clientes/$', views.listar_clientes, name='listar_clientes'),
    url(r'^clientes/adicionar/$', views.adicionar_cliente, name='adicionar_cliente'),
    url(r'^clientes/excluir/$', views.excluir_cliente, name='excluir_cliente'),
    url(r'^clientes/detalhar/$', views.detalhar_clientes, name='detalhar_clientes'),
)