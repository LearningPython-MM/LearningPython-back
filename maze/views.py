from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from user.models import Record

def stageList(request): 
    return render(request, 'maze/stageList.html')

def game(request): 
    try :
        stage = request.GET.get('stage')
        return render(request, 'maze/game.html', {'stage':stage})
    except ValueError :
        return render(request, 'mage/stageList.html')

@csrf_exempt
def result_save(request): 
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        stage_level = request.POST.get('stage_level')
        score = request.POST.get('score')
        code = request.POST.get('code')
        complexity = request.POST.get('complexity')
        record = Record(
            user_id = user_id,
            stage_level = stage_level,
            record_score = score,
            record_code = code,
            record_complexity = complexity,
        )
        record.save()
        return render(request, 'mage/stageList')


def maze_py(request): 
    return render(request, 'maze/maze.py')

def game_py(request): 
    return render(request, 'maze/game.py')

def stageList_py(request): 
    return render(request, 'maze/stageList.py')