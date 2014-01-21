from django.forms import ModelForm, TextInput
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Event

class EventForm(ModelForm):
    class Meta:
        widgets = {
            'title': TextInput(attrs={'class': 'input-mini'})
        }

class EventAdmin(ModelAdmin):
    form = EventForm

admin.site.unregister(Event)
admin.site.register(Event, EventAdmin)
