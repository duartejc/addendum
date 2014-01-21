import datetime
from haystack import indexes
from pessoas.models import PessoaFisica, PessoaJuridica

class PessoaFisicaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nome = indexes.CharField(model_attr='nome')
    cpf = indexes.CharField(model_attr='cpf')
    data_cadastro = indexes.DateTimeField(model_attr='data_cadastro')

    def get_model(self):
        return PessoaFisica

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(data_cadastro__lte=datetime.datetime.now())
  
class PessoaJuridicaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nome = indexes.CharField(model_attr='nome')
    cnpj = indexes.CharField(model_attr='cnpj')
    data_cadastro = indexes.DateTimeField(model_attr='data_cadastro')

    def get_model(self):
        return PessoaJuridica

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(data_cadastro__lte=datetime.datetime.now())    