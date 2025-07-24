from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    home = "<h1 class ='middle '> Home Page </h1>  "
    return  HttpResponse(home)

def aboutus(request):
    aboutus = "about us Lemon <h1> about us </h1> "
    return HttpResponse(aboutus)

def contact(request):
    contact = "<h1> Contact Us  </h1> "
    return HttpResponse(contact)
