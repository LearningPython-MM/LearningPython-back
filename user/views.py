from django.shortcuts import render
from django.http import HttpResponse


def index(request): 
    return render(request, 'user/index.html')

def mypage(request): 
    return render(request, 'user/mypage.html')