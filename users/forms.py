from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

#classes for custom login
class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _("You have entered an incorrect username and password, or your account is not active."),
        'inactive': _("This account is inactive."),

    }

class MyLoginView(LoginView):
    authentication_form = MyAuthForm