from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
import logging


logger = logging.getLogger(__name__)


def login_form(request):
    if request.user.is_authenticated:
        return redirect('/posts/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/posts/')
            else:
                messages.warning(
                    request,
                    "Invalid password or username"
                )

    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, 'account/login.html', context)


def register_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('/posts/')
        messages.warning(
            request,
            "Unsuccessful registration. Invalid information"
        )

    form = UserForm()
    context = {
        "form": form,
    }
    return render(request, 'account/register.html', context)


def logout_form(request):
    logout(request)
    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, 'account/login.html', context)
