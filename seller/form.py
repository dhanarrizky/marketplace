from django.views.generic import ListView, CreateView
from guestWebsite.models import goods_for_sale, category
from django import forms
from django.contrib.auth.models import User

class postForm(forms.ModelForm):
    #user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden','value':'','class':'form-control', 'id':'elder'}))
    category = forms.ModelChoiceField(queryset=category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    stock = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = goods_for_sale
        fields = ('user','category','name','price','description','stock','image')
        widgets = {
            'user':forms.TextInput(attrs={'type':'hidden','value':'','class':'form-control', 'id':'elder'})
        }
        