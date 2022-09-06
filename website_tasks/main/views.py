from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>Hello</h4>')


def text(request):
    return HttpResponse('<h4>It"s cool!</h4>')
