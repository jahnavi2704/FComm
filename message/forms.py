from django.contrib.auth.models impot User
from django import forms

class UserForm(forms.ModelForm):
    passsword=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model-User
        fields=['username','email','password']
        
