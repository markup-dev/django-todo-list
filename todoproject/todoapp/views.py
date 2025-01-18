from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Task


def todoapp(request):
	all_tasks = Task.objects.all()
	return render(request, 'todolist.html', {'all_tasks': all_tasks})


def add_task(request):
	task = Task()
	task.title = request.POST['title']
	task.description = request.POST['description']
	task.priority = request.POST['priority']
	task.save()
	return HttpResponseRedirect('/todoapp/')


def delete_task(request, id):
	task = Task.objects.get(id=id)
	task.delete()
	return HttpResponseRedirect('/todoapp/')
