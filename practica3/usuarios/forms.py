from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'cui', 'profesion', 'password1', 'password2']

class AccesoForm(AuthenticationForm):
    pass
 
