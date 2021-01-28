from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>ello :P</h2>')


def about(request):
    return HttpResponse('<h1>About</h2>')

