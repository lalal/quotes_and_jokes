from django.shortcuts import render
from django.http import HttpResponse
import requests
from api_keys import api_keys

def index(request):
    return HttpResponse("Joke of the Day")

def quote_of_the_day(request):
    print(api_keys.dad_jokes_headers)
    return HttpResponse("Quote of the Day")

def relig_quote_of_the_day(request):
    return HttpResponse("Religious quote of the Day")
