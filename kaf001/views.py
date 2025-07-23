from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request ):
    Content = "<html><body> <h1> Hello form Kaf001 app by hammad </h1> </body> </html>"
    return HttpResponse(Content)



