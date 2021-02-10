from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.contrib.auth.models import User


#fake posts Dummy_Data
# posts = [
#     {
#         'title': 'title1',
#         'content': 'abcdefghijklmnopqrstuvwxyz',
#         'date': 'Jan 28, 2021'

#     }
# ]


# def home(request):

#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/index.html', context)

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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['Title', 'Content']




class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['Title', 'Content']


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    fields = ['Title', 'Content']

    success_url = '/'



def about(request):
    return render(request, 'blog/about.html')


def junk(request):
#     context = {
#     'posts': Post.objects.all().order_by('-Date')
# }
    
    return render(request, 'blog/junk2.html')