from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user.forms import UserForm
from .models import Record

def join(request): 
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/maze/stageList')
    else:
        form = UserForm()
    return render(request, 'user/join.html', {'form': form})

def mypage(request): 
    user_info = request.user
    if user_info.is_authenticated :
        record_st0 = Record.objects.filter(user_id=request.user, stage_level=0)
        record_st1 = Record.objects.filter(user_id=request.user, stage_level=1)
        record_st2 = Record.objects.filter(user_id=request.user, stage_level=2)
        record_st3 = Record.objects.filter(user_id=request.user, stage_level=3)
        record_st4 = Record.objects.filter(user_id=request.user, stage_level=4)

        data = [record_st0, record_st1, record_st2, record_st3, record_st4]
        return render(request, 'user/mypage.html', {'record_st0':record_st0, 'record_st1':record_st1, 'record_st2':record_st2, 'record_st3':record_st3, 'record_st4':record_st4})
    else:
        return redirect('/user/login')
    
def home(request): 
    user_info = request.user
    print(user_info)
    if user_info.is_authenticated :
        return redirect('/user/mypage')
        #return render(request, 'user/home.html')
    else:
        return redirect('/user/login')