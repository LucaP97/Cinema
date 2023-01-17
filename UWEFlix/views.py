from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home(request):
    return HttpResponse("hello world")

def hello_there(request):
    
    name = 'Luca'
    
    return render(
        request,
        'UWEFlix/hello_there.html',
        {
            'name': name,
            'date': datetime.datetime.now()
        }
    )

def home(request):
    return render(request, "UWEFlix/home.html")

def about(request):
    return render(request, "UWEFlix/about.html")

def contact(request):
    return render(request, "UWEFlix/contact.html")
