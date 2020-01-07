from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the index action.")

def hello(request):
    return HttpResponse("Hello world!")

