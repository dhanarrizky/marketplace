from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class regisForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-lg", "placeholder":"Username", "name":"username"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={"type":"password","class":"form-control form-control-lg", "placeholder":"password1", "name":"password1"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={"type":"password","class":"form-control form-control-lg", "placeholder":"password2", "name":"password2"}))
    
    class Meta:
        model = User
        fields = ("username","password1","password2")
        
        