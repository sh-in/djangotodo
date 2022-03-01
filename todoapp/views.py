from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView

from .models import Todoapp

# Create your views here.
class TodoappList(ListView):
    model = Todoapp
    context_object_name = "tasks"