from django.urls import path

from . import views

app_name = 'basket' # quick reference point for url patterns below. Usefull in reverse

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),  
    path('add/', views.basket_add, name='basket_add'),
    
]
