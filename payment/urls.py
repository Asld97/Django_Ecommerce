from django.urls import path
from . import views

app_name = 'payment' # quick reference point for url patterns below. Usefull in reverse

urlpatterns = [
    
    path('', views.BasketView, name='basket'),
    path('orderplaced/', views.order_placed, name='order_placed'),
    # path('error', views.Error.as_view(), name='error'),
    path('webhook/', views.stripe_webhook),

]
