from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.exceptions import ValidationError
#         from django import forms

from django.db import models

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#         widgets = {
#             'username':forms.TextInput(attrs={'class':'form-control'}),
#             'email':forms.TextInput(attrs={'class':'form-control'}),
#             'password1':forms.PasswordInput(attrs={'class':'form-control'}),
#             'password2':forms.TextInput(attrs={'class': 'form-control'}),
#         }


