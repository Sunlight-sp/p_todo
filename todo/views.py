from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Todo
from .forms import *


###############################################
'''
def home(request):
    tasks = Todo.objects.all().order_by('-pk')
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)
'''

def home(request):
    #username=request.user
    #user = User.objects.filter(username=username)
    # tasks = Todo.objects.filter(user=user[0])
    # tasks = Todo.objects.all().order_by('-pk')

    user=request.user
    tasks = Todo.objects.filter(user=user).order_by('-pk')
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)

def add(request):
    if request.method == 'POST':
        user_=request.user
        title_ = request.POST.get('title')
        print(user_,title_)
        todo_obj = Todo(user=user_,title=title_)
        todo_obj.save()
        messages.success(request, "successfully added")
        return redirect('/todo')


def delete(request, taskId):
    post_ = Todo.objects.filter(pk=taskId)  # pk=primary key

    post_.delete()
    messages.info(request, 'list deleted')
    return redirect('/todo')


def edit(request, taskId):
    task = Todo.objects.get(id=taskId)

    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/todo')

    context = {'form': form}

    return render(request, 'todo/update_task.html', context)


def complete(request, taskId):
    task = Todo.objects.get(pk=taskId)

    task.complete = True
    task.save()
    messages.success(request, "Marked as completed")
    return redirect('/todo')


def uncomplete(request, taskId):
    task = Todo.objects.get(pk=taskId)

    task.complete = False
    task.save()
    messages.success(request, "Marked as completed")
    return redirect('/todo')
