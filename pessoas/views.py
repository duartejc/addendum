from django.http import HttpResponse
from django.template import RequestContext, loader
from pessoas.models import Pessoa
from common.forms import FormEndereco

def listar_clientes(request):
    clientes = Pessoa.objects.order_by('nome')[:5]
    context = RequestContext(request, {
        'modulo': 'Clientes',                               
        'clientes': clientes,
    })
    template = loader.get_template('clientes/listar.html')
    return HttpResponse(template.render(context));

def adicionar_cliente(request):
    form = FormEndereco()
    context = RequestContext(request, {
        'modulo': 'Clientes',
        'form_endereco': form,                     
    })
    template = loader.get_template('clientes/editar.html')
    return HttpResponse(template.render(context));

def excluir_cliente(request):
    context = RequestContext(request, {
        'modulo': 'Clientes',                               
    })
    template = loader.get_template('clientes/excluir.html')
    return HttpResponse(template.render(context));

def detalhar_clientes(request):
    context = RequestContext(request, {
        'modulo': 'Clientes',                               
    })
    template = loader.get_template('clientes/detalhar.html')
    return HttpResponse(template.render(context));
    
