from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import UserForm


def index(request): 
    return render(request, 'user/index.html')

def join(request): 
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'user/join.html', {'form': form})

def mypage(request): 
    return render(request, 'user/mypage.html')
    
def home(request): 
    return render(request, 'user/home.html')