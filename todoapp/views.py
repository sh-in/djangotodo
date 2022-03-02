from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from django.urls import reverse_lazy

from .models import Todoapp

# Create your views here.
class TodoappList(ListView):
    model = Todoapp
    context_object_name = "tasks"

class TodoappDetail(DetailView):
    model = Todoapp
    context_object_name = "task"

class TodoappCreate(CreateView):
    model = Todoapp
    fields = "__all__"
    success_url = reverse_lazy("list")