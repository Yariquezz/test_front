from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label="User Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "User Name"
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]
