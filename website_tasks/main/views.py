from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all().order_by('title')
    text = {
        'tasks': tasks
    }
    return render(request, 'index.html', text)


def about(request):
    return render(request, 'about.html')


def detail(request, pk):
    task = Task.objects.get(pk=pk)
    context = {
        'task': task
    }
    return render(request, 'detail.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной!'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)

