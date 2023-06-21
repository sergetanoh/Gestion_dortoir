from django.urls import path
from .views import login_view,logout_view

urlpatterns=[
    path('login',login_view,name='login-blog'),
    path('deconnexion',logout_view,name='logout1'),
    

]