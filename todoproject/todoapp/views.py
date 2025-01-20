from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def task_list(request):
	tasks = Task.objects.filter(user=request.user).order_by('priority', 'done')
	user = request.user
	return render(request, 'todolist.html', {'tasks': tasks, 'user': user})


@login_required
def add_task(request):
	if request.method == 'POST':
		task = Task()
		task.description = request.POST['description'].strip()
		task.priority = request.POST['priority']
		task.user = request.user
		task.save()
		return HttpResponseRedirect('/')


@login_required
def delete_task(request, i):
	task = Task.objects.get(id=i)
	task.delete()
	return HttpResponseRedirect('/')


@login_required
def delete_all_tasks(request):
	tasks = Task.objects.filter(user=request.user)
	for task in tasks:
		task.delete()
	return HttpResponseRedirect('/')


@login_required
def done_task(request, i):
	task = Task.objects.get(id=i)
	task.done = True
	task.save()
	return HttpResponseRedirect('/')
