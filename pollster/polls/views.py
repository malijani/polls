""" Views of polls app which renders output """
from django.shortcuts import render

from .models import Question, Choice


def index(request):
    """ Get questions and display them """
    template = 'polls/index.html'
    context = {

    }
    return render(request, template, context)
