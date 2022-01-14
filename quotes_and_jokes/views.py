from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Root url")

def redirct_view(request):
    response = redirect('/of_the_day/')
    return response
