from django.contrib import admin
from django.urls import path
from .views import waves_events,event_detail

urlpatterns = [

    path('events/<slug:category_slug>',waves_events,name='events_by_category'),
    path('events/<slug:category_slug>/<slug:event_slug>',event_detail,name='event_detail')

]
