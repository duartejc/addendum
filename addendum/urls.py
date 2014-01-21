from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^calendario/', include('calendario.urls', namespace='calendario')),
    url(r'^pessoas/', include('pessoas.urls', namespace='pessoas')),
    url(r'^search/', include('haystack.urls')),
)
