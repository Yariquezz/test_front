from django.shortcuts import render, HttpResponse, Http404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from .forms import LoginForm
from .models import Post
import logging


logger = logging.getLogger(__name__)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/posts.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


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
