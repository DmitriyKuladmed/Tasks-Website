from django.shortcuts import render
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


def create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

