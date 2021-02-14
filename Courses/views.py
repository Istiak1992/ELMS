from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from .models import Course
from Lessons.models import Lesson
from Questions.models import Question

def Home(request):
	context = {}
	return render(request, "Courses/home.html", context)

def Register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="Courses/register.html", context={"register_form":form})

def Login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="Courses/login.html", context={"login_form":form})

def Logout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")


def ShowCourse(request):
	courses = Course.objects.all()
	context = {"courses":courses}

	return render(request, "Courses/showcourse.html", context)

def ShowLesson(request, pk):
	course = Course.objects.get(id=pk)
	lessons = Lesson.objects.filter(course=course)
	context = {"lessons":lessons, "course":course}

	return render(request, "Courses/showlessons.html", context)

def ShowQuestion(request, pk):
	lesson = Lesson.objects.get(id=pk)
	questions = Question.objects.filter(lesson=lesson)
	context = {"lesson":lesson, "questions":questions}

	return render(request, "Courses/showquestion.html", context)

def QuestionRadio(request):
	if request.method == "POST":
		print(request)
	return render(request=request, template_name="Courses/showquestion.html")