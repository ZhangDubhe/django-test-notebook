from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('collect', views.collect, name='collect'),
    path('quiz', views.quiz, name='quiz'),
    path('account/login', views.init_login, name="login"),
    path('account/login-post', views.login, name="login-post"),
    path('account/register',views.init_register, name="register"),
    path('account/register-post',views.register, name="register-post"),
]