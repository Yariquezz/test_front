from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.login_form, name='login'),
    path('logout/', views.logout_form, name='logout'),
    path('posts/', views.posts, name='posts'),
]
