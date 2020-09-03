from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=180)
    password = forms.CharField(widget=forms.PasswordInput)