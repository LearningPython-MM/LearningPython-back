from django.shortcuts import render
from django.http import HttpResponse


def stageList(request): 
    return render(request, 'maze/stageList.html')

def game(request): 
    try :
        stage = request.GET.get('stage')
        return render(request, 'maze/game.html', {'stage':stage})
    except ValueError :
        return render(request, 'mage/stageList.html')

def maze_js(request): 
    return render(request, 'maze/maze.js')

def maze_py(request): 
    return render(request, 'maze/maze.py')

def game_css(request): 
    return render(request, 'maze/game.css')

def game_py(request): 
    return render(request, 'maze/game.py')

def stageList_py(request): 
    return render(request, 'maze/stageList.py')

def ground_png(request): 
    return render(request, 'maze/image/ground.png')

def miggyung_png(request): 
    return render(request, 'maze/image/miggyung.png')

def other_png(request): 
    return render(request, 'maze/image/other.png')

def grace_png(request): 
    return render(request, 'maze/image/grace.png')

def potal_png(request): 
    return render(request, 'maze/image/potal.png.')

def waterballun_png(request): 
    return render(request, 'maze/image/waterballun.png.')