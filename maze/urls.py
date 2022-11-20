from django.urls import path

from . import views

urlpatterns = [
    path('', views.stage, name='stage'),
    path('maze/', views.maze, name='maze'),
]