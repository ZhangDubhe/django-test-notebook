from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import User, Question, Type
# Other Plugin
import json
from django.db.models import Q
import random
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
			questions = load_question_by(user.id)
			return render(request, 'index.html', {
				'title': 'Home',
				'user': user,
				'info': 'Base',
				'type_content': types,
				'questions': questions
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
		user = User.objects.get(Q(id=user_id) | Q(id=1))
		print(40 * "*")
		print("user", user)
	except User.DoesNotExist:
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
	except User.DoesNotExist:
		return render(request, 'login.html', {
			'title': 'Login',
			'other': 'Auth error'
		})
	types = load_type_content(user.id)
	return render(request, 'collect.html', {
		'title': 'Home',
		'user': user,
		'info': 'Base',
		'type_content': types
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
		except User.DoesNotExist:
			msg = " No this user. "
			return render(request, 'login.html', {
				'title': '重新登录',
				'info': '登录',
				'other': msg
			})
	types = load_type_content(user.id)
	try:
		current_question = Question.objects.get(id=question_id)
	except Question.DoesNotExist:
		questions = load_question_by(user.id)
		return render(request, 'index.html', {
			'title': 'Home',
			'user': user,
			'info': 'Base',
			'type_content': types,
			'questions': questions
		})
	right_answer = current_question.right_answer
	wrong_answers = json.loads(current_question.wrong_answer)
	ans_text = {
		1: right_answer,
		2: wrong_answers['wrong1'],
		3: wrong_answers['wrong2'],
		4: wrong_answers['wrong3']
	}
	ans_index = [1, 2, 3, 4]

	random.shuffle(ans_index)
	print("[ + ] index:", ans_index)
	print("[ + ] text:", ans_text)
	return render(request, 'question.html', {
		'title': '错题第'+str(current_question.id) + '号',
		'username': user.user_name,
		'user': user,
		'question': current_question,
		'type_content': types,
		'answers': ans_text,
		'answers_index': ans_index,
		'secret': right_answer
	})


def load_type_content(user_id):
	try:
		types = Type.objects.filter(user__id=user_id)
	except Type.DoesNotExist:
		types = ''
	return types


def load_question_by(user_id):
	try:
		questions = Question.objects.filter(user__id=user_id)
	except Question.DoesNotExist:
		questions = None
	return questions


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
	elif request.method == "POST" and request.POST.get('question_type') and request.POST.get('question'):
		problem = request.POST.get('question')
		right = request.POST.get('rightAns')
		wrong1 = request.POST.get('wrongAns1')
		wrong2 = request.POST.get('wrongAns2')
		wrong3 = request.POST.get('wrongAns3')
		wrong_ans = json.dumps({
			"wrong1": wrong1,
			"wrong2": wrong2,
			"wrong3": wrong3
		})
		type_id = request.POST.get('question_type')
		type_name = Type.objects.get(id=type_id).name
		try:
			new_question = Question(name=problem, right_answer=right, wrong_answer=wrong_ans, question_type=type_name, user_id=user_id)
			new_question.save()
			result = "Already update - " + problem + "- into System."
			status = 21
		except Question.DoesNotExist:
			result = "You update new question? But we don't added this function."
			status = 0
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
			'status': status,
			'questionid': new_question.id
		}))
	else:
		return HttpResponse(json.dumps({
			'result': result,
			'status': status
		}))


def check_user_valid(user_id):
	return True


def delete_items(request, user_id):
	if request.method == "POST" and request.POST.get('questions') and check_user_valid(user_id):
		questions = json.loads(request.POST.get('questions'))
		print('[ + ] POST  | question:', questions)
		for each in questions:
			print('[ - ] Delete  | question:', each)
			del_question = Question.objects.filter(id=each).delete()
		status = 20
	else:
		status = 0
	return HttpResponse(json.dumps({
		'status': status
	}))



