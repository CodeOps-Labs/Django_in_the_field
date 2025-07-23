from django.urls import path
from . import views

# mapping the view here

urlpatterns = [
    path('', views.home),
]