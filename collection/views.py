from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Other Plugin
import json

# Create your views here.

def index(request):
    return render(request, 'register.html', {
			'title': 'Sign up or Log'
		})

def collect(request):
    return render(request, 'quiz.html', {
			'title': 'Quiz',
			'info':"随机错题"
		})

def quiz(request):
    return render(request, 'collect.html', {
			'title': 'Collection',
			'info':"请输入你想记录的错题"
		})
    

def register(request):
    return render(request, 'register.html', {
			'title': 'Signup',
			'info':"注册"
		})
    

def login(request):
    return render(request, 'login.html', {
			'title': 'login',
			'info':"登录"
		})
    