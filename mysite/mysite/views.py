from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href='/polls'>Polls App</a>")