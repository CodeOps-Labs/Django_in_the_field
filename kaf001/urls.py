from django.urls import path

from kaf01.urls import urlpatterns
from . import views


# mapping the view here

urlpatterns = [
    path ('', views.home),
]