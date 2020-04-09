""" URLs configuration for pages app """
from django.urls import path
from . import apps
from . import views

app_name = apps.PagesConfig.name

urlpatterns = [
    path('', views.index, name='index')
]
