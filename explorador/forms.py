from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms


class QrForm(ModelForm):
    class Meta:
        model = Qr
        fields = '__all__'
        
class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #ver documentación para mas campos disponibles