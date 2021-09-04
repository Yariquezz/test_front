from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.login_form, name='login'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('logout/', views.logout_form, name='logout'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('create/', views.CreatePost.as_view(), name='create'),
    path('edit/<slug:slug>/', views.EditPost.as_view(), name='edit'),
    path('delete/<slug:slug>/', views.DeletePost.as_view(), name='delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
