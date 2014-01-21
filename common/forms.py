from django import forms
from municipios.widgets import SelectMunicipioWidget    
from haystack.forms import SearchForm

class FormEndereco(forms.Form):
    municipio = forms.IntegerField(label=u"UF - Municipio", widget=SelectMunicipioWidget)
    
    
class DateRangeSearchForm(SearchForm):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)