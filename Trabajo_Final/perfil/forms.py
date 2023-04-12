from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from perfil.models import Avatar


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField(label='Editar email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]