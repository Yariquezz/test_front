from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.login_form, name='login'),
    path('register/', views.register_form, name='register'),
    path('logout/', views.logout_form, name='logout'),
]
