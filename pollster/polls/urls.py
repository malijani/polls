""" Routing core of polls app """
from django.urls import path
from . import apps, views

app_name = apps.PollsConfig.name

urlpatterns = [
    path('', views.index, name='index'),
]