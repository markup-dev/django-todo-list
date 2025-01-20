from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserLoginForm


def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Аккаунт создан для {username}')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'register.html', {'form': form})


def login_view(request):
	if request.user.is_authenticated:
		return redirect('task_list')

	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				next_url = request.GET.get('next', 'task_list')
				return redirect(next_url)
			else:
				messages.error(request, 'Неверный логин или пароль')
	else:
		form = UserLoginForm()
	return render(request, 'login.html', {'form': form})
