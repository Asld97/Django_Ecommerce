from django.urls import path, re_path
from . import views

app_name = 'account' # quick reference point for url patterns below. Usefull in reverse

urlpatterns = [
    path('register/', views.account_register, name='register'),   
    path('account/<slug:uidb64>/<slug:token>', views.account_activate, name='activate'),  
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
    #     views.account_activate, name='activate'), 
    # User dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
        
]
