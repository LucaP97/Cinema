from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def users_home(request):
    return HttpResponse('Welcome to users')

