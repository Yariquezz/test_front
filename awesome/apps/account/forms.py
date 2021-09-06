from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Ім'я користувача:",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ім'я користувача"
        })
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Пароль"
        })
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]


class UserForm(forms.ModelForm):

    username = forms.CharField(
        label="Ім'я користувача",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    confirm_password = forms.CharField(
        label="Підтіердження паролю",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )
