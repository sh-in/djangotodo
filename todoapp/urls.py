from unicodedata import name
from django.urls import path
from .views import TodoappList

urlpatterns = [
    path("", TodoappList.as_view(), name="list"),
]