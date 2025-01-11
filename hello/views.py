from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
    #return HttpResponse("Hello, world")--old/easy way, pass to name of template instead^^^

def mom(request):
    return HttpResponse("I love you")

def greet(request,name):
    #return HttpResponse(f"Hello, {name.capitalize()}!") old way, using httpresponse instead of render
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
        }
    )