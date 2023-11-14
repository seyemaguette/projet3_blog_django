from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label = 'Nom d"utilisateur',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"}))
    password1 = forms.CharField(
       label = 'Mot de passe',       
       widget=forms.PasswordInput(
            attrs={
                "class": "form-control"})) 
    password2 = forms.CharField(
       label = 'Confirmation du mot de passe',       
       widget=forms.PasswordInput(
            attrs={
                "class": "form-control"})) 
   
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        
        
class login_form(forms.Form):
    username = forms.CharField(
        label = 'Nom d"utilisateur',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"}))
    password = forms.CharField(
       label = 'Mot de passe',       
       widget=forms.PasswordInput(
            attrs={
                "class": "form-control"})) 