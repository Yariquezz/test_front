from django.shortcuts import render, HttpResponse, Http404
import logging


logger = logging.getLogger(__name__)
# Create your views here.


def home(request):
    return render(request, 'posts/index.html')
