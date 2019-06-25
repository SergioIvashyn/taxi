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


class OrderFormOperator(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['driver','client','place_from','place_to','status']

		widgets = {
				'place_from':forms.TextInput(attrs={'class':'form-control'}),
				'driver':forms.Select(attrs={'class':'form-control'}),
				'client':forms.Select(attrs={'class':'form-control'}),
				'status':forms.Select(attrs={'class':'form-control'}),
				'place_to':forms.TextInput(attrs={'class':'form-control'}),
				# 'birth':forms.SelectDateWidget(),
				# 'description':forms.Textarea(attrs={'class':'form-control'}),
				#'slug':forms.TextInput(attrs={'class': 'form-control'}),
		}	

class OrderForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = ['place_from','place_to']

		widgets = {
			'place_from':forms.TextInput(attrs={'class':'form-control'}),
			# 'group':forms.Select(attrs={'class':'form-control'}),
			'place_to':forms.TextInput(attrs={'class':'form-control'}),
			# 'birth':forms.SelectDateWidget(),
			# 'description':forms.Textarea(attrs={'class':'form-control'}),
			#'slug':forms.TextInput(attrs={'class': 'form-control'}),
		}
		labels = {
			'place_from':'Откуда',
			'place_to':'Куда',
		}
	

class OrderFormDriver(forms.ModelForm):

	class Meta:
		model = Order
		fields = ['status']

		widgets = {
			# 'place_from':forms.TextInput(attrs={'class':'form-control'}),
			'status':forms.Select(attrs={'class':'form-control'}),
			# 'place_to':forms.TextInput(attrs={'class':'form-control'}),
			# 'birth':forms.SelectDateWidget(),
			# 'description':forms.Textarea(attrs={'class':'form-control'}),
			#'slug':forms.TextInput(attrs={'class': 'form-control'}),
		}




class DriverForm(forms.ModelForm):

	class Meta:
		model = Driver
		fields = ['car']

		widgets = {
			# 'place_from':forms.TextInput(attrs={'class':'form-control'}),
			'car':forms.Select(attrs={'class':'form-control'}),
			# 'place_to':forms.TextInput(attrs={'class':'form-control'}),
			# 'birth':forms.SelectDateWidget(),
			# 'description':forms.Textarea(attrs={'class':'form-control'}),
			#'slug':forms.TextInput(attrs={'class': 'form-control'}),
		}