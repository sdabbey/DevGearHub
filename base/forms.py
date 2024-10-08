from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=True)
    email = forms.EmailField(label='Email', max_length=100, min_length=5,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             required=True)
    password1 = forms.CharField(label='Password', max_length=100, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                required=True)
    password2 = forms.CharField(label='Confirm Password',
                                max_length=100, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                required=True)
