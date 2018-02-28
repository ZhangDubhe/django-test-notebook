from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import User, Question, Type
# Other Plugin
import json


# Create your views here.


def index(request, **user_id):
	if user_id:
		print(100 * "*")
		print(100 * "*")
		print("USERID:", user_id)
		user_id = user_id['user_id']
		print("USERID:", user_id)
		try:
			user = User.objects.get(id=user_id)
			print(100 * "*")
			print("user", user)
			types = load_type_content(user.id)
			return render(request, 'index.html', {
				'title': 'Home',
				'user': user,
				'info': 'Base',
				'type_content': types
			})
		except User.DoesNotExist:
			results = "No this user?"
			print(100 * "*")
			return render(request, 'login.html', {
				'title': 'Login',
				'other': results
			})

	return render(request, 'index.html', {
		'title': 'Welcome'
	})





def quiz(request, user_id):
	try:
		user = User.objects.get(id=user_id)
		print(40 * "*")
		print("user", user)
	except:
		pass
	return render(request, 'quiz.html', {
		'title': 'Quiz',
		'info': 'Quiz',
		'username': user.user_name,
		'user': user,
	})


def collect(request, user_id):
	try:
		user = User.objects.get(id=user_id)
	except User.DoesNotExist :
		return render(request, 'login.html', {
			'title': 'Login',
			'other': 'Auth error'
		})
	return render(request, 'collect.html', {
		'title': 'Collection',
		'info': "Base",
		'user': user
	})


def init_register(request):
	return render(request, 'register.html', {
		'title': 'Signup',
		'info': "注册"
	})


def init_login(request):
	return render(request, 'login.html', {
		'title': 'login',
		'info': "登录"
	})


def register(request):
	status = 0
	if request.method == "POST" and request.POST.get('username') and request.POST.get('password'):
		username = request.POST.get('username')
		useremail = request.POST.get('email')
		userpassword = request.POST.get('password')

		try:
			is_resist_user = User.objects.get(user_name=username)
			if is_resist_user:
				results = "Already have this name, please input another."
		except User.DoesNotExist:
			try:
				user = User(user_name=username, user_email=useremail, user_password=userpassword)
				user.save()
				results = "Welcome!"
				status = 20
			except:
				results = "Create user error"
	else:
		results = "请重新输入"
	if status == 20:
		return redirect(request, user)
	else:
		return render(request, 'register.html', {
			'title': "注册",
			'info': "注册",
			'other': results
		})


def login(request):
	status = 0
	if request.method == "POST" and request.POST.get('username'):
		try:
			user = User.objects.get(user_name=request.POST.get('username'))
			if user.user_password == request.POST.get('password'):
				msg = "You're logged in."
				status = 20
			else:
				msg = "Wrong password"
		except User.DoesNotExist:
			msg = "Wrong user name, please register!"

	else:
		msg = "Wrong request"
	if status == 20:
		return redirect(request, user)
	else:
		return render(request, 'login.html', {
			'title': '重新登录',
			'info': '登录',
			'other': msg
		})


def redirect(request, user):
	return render(request, 'redirect.html', {
		'title': 'Redirecting',
		'username': user.user_name,
		'user': user,
		'content': 'Welcome, ' + user.user_name,
	})


def question(request, user_id, question_id):
	if user_id:
		try:
			user = User.objects.get(pk=user_id)
		except:
			pass
	return render(request, 'index.html', {
		'title': 'Home',
		'username': user.user_name,
		'user': user
	})


def load_type_content(user_id):
	try:
		types = Type.objects.filter(user__id=user_id)
	except:
		types = ''
	return types

def add_items(request, user_id):
	if request.method == "POST" and request.POST.get('type') and not request.POST.get('question'):
		editor = user_id
		new_type = request.POST.get('type')
		try:
			added_type = Type(user_id=editor, name=new_type)
			added_type.save()
			result = 'Type created'
			status = 20
		except Type.DoesNotExist:
			result = 'Add failed: editor = '+str(user_id)+'type='+new_type
			status = 0
	elif request.method == "POST" and request.POST.get('type') and request.POST.get('question'):
		result = "You update new question? But we don't added this function."
		status = 21
	else:
		result = "Request error"
		status = 500

	if status == 20:
		return HttpResponse(json.dumps({
			'result': result,
			'status': status,
			'typeid': added_type.id
		}))
	elif status == 21:
		return HttpResponse(json.dumps({
			'result': result,
			'status': status
		}))
	else:
		return HttpResponse(json.dumps({
			'result': result,
			'status': status
		}))