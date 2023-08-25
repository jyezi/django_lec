from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    # name = forms.CharField(label='이름')
    class Meta:
        model = User
        # fields = ("name", "username", "password1", "password2", "email")
        fields = ("last_name", "first_name","username", "password1", "password2", "email")

        labels = {
            "last_name" : "성",
            "first_name" : "이름",
            "username" : "아이디",
            "password1" : "비밀번호",
            "password2" : "비밀번호 확인",
            "email" : "이메일",
        }

# class MypageForm(UserChangeForm):
#     password = None
#     email = forms.EmailField()
#     username = forms.IntegerField()
#     class Meta:
#         model = User
#         fields = ("username", "password")
