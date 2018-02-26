from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('collect', views.collect, name='collect'),
    path('quiz', views.quiz, name='quiz'),
    path('account/login', views.login, name='login'),
    path('account/register', views.register, name='register')
]