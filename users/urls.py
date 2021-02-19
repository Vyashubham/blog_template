from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileCreateView, ProfileDeleteView, ProfileUpdateView

urlpatterns = [
    path('register/', views.register, name="register_view" ),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login_view" ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout_view" ),
    path('account/', views.account, name="account" ),
    path('profile/', views.profile, name="profile" ),
    path('new/', ProfileCreateView.as_view(), name="profile_create_view"),
]
