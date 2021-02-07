from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
urlpatterns = [
    # path('', views.home, name="website_home"),
    path('', PostListView.as_view(), name="website_home"),
    path('post/<slug:slug>/', PostDetailView.as_view(), name="post_detail_view"),
    path('new/', PostCreateView.as_view(), name="post_create_view"),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name="post_update_view"),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name="post_delete_view"),
    path('user/<str:username>', UserPostListView.as_view(), name="user_detail_view"),
    path('about/', views.about, name="about"),
]
