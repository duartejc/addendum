from pessoas.models import PessoaFisica
from django.shortcuts import render_to_response

def search(request):
        query = request.GET.get('q', '')
        posts = PessoaFisica.search.query(query)
        return render_to_response('searchengine/busca.html',
                                  {'posts': posts, 'query': query,})