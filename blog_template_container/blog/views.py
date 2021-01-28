from django.shortcuts import render
from django.http import HttpResponse

#fake posts Dummy_Data
posts = [
    {
        'title': 'title1',
        'content': 'abcdefghijklmnopqrstuvwxyz',
        'date': 'Jan 28, 2021'

    }
]




def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')

