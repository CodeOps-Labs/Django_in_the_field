from django.urls import  path
from . import views

urlpatterns =[
    path('home', views.home, name = 'home'),
    path('about', views.aboutus, name = 'about us '),
    path('contact', views.contact, name = 'contact us '),
]