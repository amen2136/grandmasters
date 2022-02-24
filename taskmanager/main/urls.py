from re import template
from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus', views.about, name='info'),
    path('addform', views.create, name='form'),
    path('addnews', views.news, name='new_s'),
    path('createtodolist', views.todolist, name='todo'),
]
