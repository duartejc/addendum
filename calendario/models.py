from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=80)
    allDay = models.BooleanField(default=False)
    start = models.DateTimeField(null=False)
    end = models.DateTimeField(null=True)
    url = models.CharField(max_length=50)
    className = models.CharField(max_length=20)
    editable = models.BooleanField(default=True)
    startEditable = models.BooleanField(default=True)
    durationEditable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        verbose_name_plural = "eventos"


### Admin

class EventAdmin(admin.ModelAdmin):
    list_display = ["creator", "start", "title", "end"]
    list_filter = ["creator"]

admin.site.register(Event, EventAdmin)