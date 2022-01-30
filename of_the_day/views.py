from django.shortcuts import render
from django.http import HttpResponse
import requests
from api_keys import api_keys
from .models import Otd
from datetime import datetime

otd_types = ("joke", "quote")
sub_types = ("religious", "motivational", "quote_trivia", "joke")

def index(request):
    now = datetime.now()
    ymd = now.strftime("%Y-%m-%d")
    joke_otd = Otd.objects.filter(otd_date=ymd).filter(otd_type="joke").filter(sub_type="joke")
    if joke_otd.count() == 0:
        response = requests.request("GET", api_keys.dad_jokes_url, headers=api_keys.dad_jokes_headers)
        joke_otd = Otd(otd_type = "joke", sub_type = "joke", api_source="Dad Jokes", data=response.text, otd_date=ymd)
        joke_otd.save()
    else:
        joke_otd = joke_otd.first()


    print(joke_otd)

    return render(request, "joke_of_the_day.html", {'joke_otd': joke_otd})

def quote_of_the_day(request):
    print(api_keys.dad_jokes_headers)
    return HttpResponse("Quote of the Day")

def relig_quote_of_the_day(request):
    return HttpResponse("Religious quote of the Day")
