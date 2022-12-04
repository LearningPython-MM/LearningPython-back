from django.urls import path

from . import views

app_name = 'maze'

urlpatterns = [
    path('stageList', views.stageList, name='stageList'),
    path('game', views.game, name='game'),

    path('maze.js', views.maze_js),
    path('maze.py', views.maze_py),
    path('game.css', views.game_css),
    path('game.py', views.game_py),
    path('stageList.py', views.stageList_py),
    path('image/ground.png', views.ground_png),
    path('image/miggyung.png', views.miggyung_png),
    path('image/other.png', views.other_png),
    path('image/grace.png', views.grace_png),
    path('image/potal.png', views.potal_png),
    path('image/waterballun.png', views.waterballun_png),
]