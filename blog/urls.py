from django.urls import path
from .views import PostListView, PostDetailView, BlogpostListView

urlpatterns = [
    
    path('', PostListView.as_view(), name="website_home"),
    path('blog/', BlogpostListView.as_view(), name="blog_index"),
    path('post/<slug:slug>/', PostDetailView.as_view(), name="post_detail_view"),
    
]
