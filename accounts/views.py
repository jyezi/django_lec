from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm, MypageForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form':form})

# def mypage(request):
#     if request.method == "POST":
#         form = MypageForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/')
#     else:
#         form = MypageForm()
#     return render(request, 'accounts/mypage.html', {'form':form})

def mypage(request):
    if request.method == "POST":
        mypageForm = MypageForm(request.POST, instance=request.user)
        if mypageForm.is_valid():
            user = mypageForm.save()
            login(request, user)
            #messages.success(request, '회원정보가 수정되었습니다.')
            return redirect('/')
    else:
        mypageForm = MypageForm(instance=request.user)
    return render(request, 'accounts/mypage.html', {'mypageForm':mypageForm})