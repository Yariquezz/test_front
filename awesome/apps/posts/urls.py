from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.login_form, name='login'),
    path('logout/', views.logout_form, name='logout'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
