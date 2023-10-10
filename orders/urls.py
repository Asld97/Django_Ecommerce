from django.urls import path
from . import views

app_name = 'orders' # quick reference point for url patterns below. Usefull in reverse

urlpatterns = [
    
    path('add/', views.add, name='add'),
 

]
