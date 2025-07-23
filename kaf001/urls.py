from django.urls import path
from . import views

# mapping the view here

urlpatterns = [
    path('', views.home),
    path('txt', views.returntxt),
    path('user/<str:username>/<int:userid>/', views.user_detail, name='user_detail'),
    # mapping urls using params
    path('cars/<str:car>', views.menuitems)# dish =pasta
]