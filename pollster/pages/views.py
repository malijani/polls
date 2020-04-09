""" Pages application views """
from django.shortcuts import render

def index(request):
    """ Just renders a page for / """
    template = 'pages/index.html'
    return render(request, template)
