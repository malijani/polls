""" Routing core of polls app """
from django.urls import path
from . import apps, views

app_name = apps.PollsConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    ]
