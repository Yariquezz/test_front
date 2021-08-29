from django import forms
from django.contrib.auth.models import User
from .models import Post


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


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
        })
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "author",
            "status"
        ]
        widget = {
            "author": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


class EditPostForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
        })
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
