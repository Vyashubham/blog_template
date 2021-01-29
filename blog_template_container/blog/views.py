from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#fake posts Dummy_Data
# posts = [
#     {
#         'title': 'title1',
#         'content': 'abcdefghijklmnopqrstuvwxyz',
#         'date': 'Jan 28, 2021'

#     }
# ]


def home(request):

    context = {
        'posts': Post.objects.all()
    }


    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')

