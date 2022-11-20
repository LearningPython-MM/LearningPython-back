from django.shortcuts import render
from django.http import HttpResponse


def stage(request): 
    return render(request, 'maze/stage.html')

def maze(request): 
    return render(request, 'maze/index.html')

def maze_js(request): 
    return render(request, 'maze/maze.js')

def maze_py(request): 
    return render(request, 'maze/maze.py')