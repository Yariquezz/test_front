from django.shortcuts import render, HttpResponse, Http404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
import logging


logger = logging.getLogger(__name__)


def login_form(request):

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

    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, 'posts/index.html', context)


def logout_form(request):
    logout(request)
    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, 'posts/index.html', context)


def posts(request):

    return render(request, 'posts/posts.html')
