from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('join/', views.join, name='join'),

    path('mypage', views.mypage, name='mypage'),
    path('home', views.home, name='home')
]