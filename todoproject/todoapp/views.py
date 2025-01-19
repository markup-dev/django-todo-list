from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Task


def todoapp(request):
	all_tasks = Task.objects.all()
	return render(request, 'todolist.html', {'all_tasks': all_tasks})


def add_task(request):
	task = Task()
	task.description = request.POST['description']
	task.priority = request.POST['priority']
	task.save()
	return HttpResponseRedirect('/')


def delete_task(request, i):
	task = Task.objects.get(id=i)
	task.delete()
	return HttpResponseRedirect('/')
