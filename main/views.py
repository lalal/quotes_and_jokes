from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.shortcuts import redirect

def index(request):
    return render(request, 'main/home.html')

def redirct_view(request):
    response = redirect('/of_the_day/')
    return response
