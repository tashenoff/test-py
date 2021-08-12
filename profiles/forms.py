from django import forms
from django.forms import widgets
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2' )

class LoginForm():
    
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2' )

