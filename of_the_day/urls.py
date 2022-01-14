from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='joke_of_the_day'),
    path('quote/', views.quote_of_the_day, name='quote_of_the_day'),
    path('relig_quote/', views.relig_quote_of_the_day, name='relig_quote_of_the_day')

]
