from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse("Welcome home\n this is hammad \n <h1> Hammad </h1>  <span> Django </span > ")
