from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('addblog/', views.addblog, name='addblog'),
    path('blogpost/<int:id>', views.blogpost, name='blogpost'),
    path('', views.blog, name='blog'),
]
