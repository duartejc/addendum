from django.db import models
from djoosh import SearchMixin
from django.core import urlresolvers

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)
    #TODO municipio =
    observacao = models.CharField(max_length=300)
    data_cadastro = models.DateTimeField()
    
    def get_absolute_url(self):
        return urlresolvers.reverse('pessoas:detalhar_clientes')
    
    def __unicode__(self):
        return self.nome
        
class PessoaFisica(Pessoa, SearchMixin):
    SEXO = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=SEXO)
    nascimento = models.DateField()
    
class PessoaJuridica(Pessoa, SearchMixin):
    cnpj = models.CharField(max_length=14)
    inscricao_estadual = models.CharField(max_length=25)
    razao_social = models.CharField(max_length=250)