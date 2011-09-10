# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from frontend.models import Usuario

class LoginForm(forms.Form):
    """
    formulaio de logeo de usario
    username/password logins.
    @author jessica
    """
    username = forms.CharField(label="Nombre de Usuario", max_length=30)
    password = forms.CharField(label="contraseña", widget=forms.PasswordInput)

class RegistroForm(forms.ModelForm):
    """
    ss
    """
    username = forms.CharField(label="Nombre de Usuario", max_length=30)
    password = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    first_name =forms.CharField(label="Nombres", max_length=30)
    last_name =forms.CharField(label="Apellidos", max_length=30)
    email =forms.EmailField(label="E-Mail", max_length=30)
    #event = models.ForeignKey(Event, related_name="subscribers")
    class Meta:
        model = Usuario
        exclude = ['is_staff','is_active','groups',
            'last_login','date_joined',
            'is_superuser','user_permissions'
        ]
