from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('u/<int:user_id>/', views.index, name='logged'),
    path('u/<int:user_id>/collect', views.collect, name='collect'),
    path('u/<int:user_id>/collect/add/', views.add_items),
    path('u/<int:user_id>/collect/delete/', views.delete_items),
    path('u/<int:user_id>/quiz', views.quiz, name='quiz'),
    path('u/<int:user_id>/question/<int:question_id>', views.question, name='question'),
    path('account/login', views.init_login, name="login"),
    path('account/login-post', views.login, name="login-post"),
    path('account/register', views.init_register, name="register"),
    path('account/register-post', views.register, name="register-post"),

]