from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):

    list_display = ('event_name','category','description','date','rounds','rules','contact','price',)
    prepopulated_fields = {'slug':('event_name',)}

admin.site.register(Event,EventAdmin)