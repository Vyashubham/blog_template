from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.models import User



class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-Date']

    paginate_by = 2 #change this to a higher number

class BlogpostListView(ListView):
    model = Post
    template_name = 'blog/blog_index.html'
    context_object_name = 'posts'
    ordering = ['-Date']

    paginate_by = 2 #change this to a higher number

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-Date']

    paginate_by = 2 #change this to a higher number

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects(username=user).order_by('-Date')


class PostDetailView(DetailView):
    model = Post

