from django.urls import URLPattern, path

from .views import team

urlpatterns = [
    path('<slug:waves_team>',team,name='team'),
]