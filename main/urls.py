from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug>', views.detail, name='detail'),
    path('posts/<slug>', views.posts, name='posts'),
]
