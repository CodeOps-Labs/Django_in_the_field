from django.urls import path
from . import views

urlpatterns = [
    path('devices/<str:phone>', views.menurad) # to show that phone = samsung
]