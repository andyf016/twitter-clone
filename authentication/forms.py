from django import forms
from twitteruser.models import CustomUser

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
    bio = forms.Textarea()
    age = forms.IntegerField()
    location = forms.CharField(max_length=180)
    birthday = forms.DateField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
