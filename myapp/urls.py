from django.urls import path
from . import views

urlpatterns = [
    path('',views.userlogin,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home')
]