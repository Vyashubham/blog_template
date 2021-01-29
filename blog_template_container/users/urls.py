from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="reigster_page_test" )
]
