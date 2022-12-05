from django.urls import path

from . import views

app_name = 'maze'

urlpatterns = [
    path('stageList', views.stageList, name='stageList'),
    path('game', views.game, name='game'),
    path('result_save', views.result_save, name='result_save'),

    path('maze.py', views.maze_py),
    path('game.py', views.game_py),
    path('stageList.py', views.stageList_py),
]