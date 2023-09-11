from django.urls import path
from . import views

app_name = 'store' # quick reference point for url patterns below. Usefull in reverse

urlpatterns = [
    path('', views.all_products, name='all_prodcuts'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list')
    
    
]