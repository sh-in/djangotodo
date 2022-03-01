from unicodedata import name
from django.urls import path
from .views import TodoappDetail, TodoappList

urlpatterns = [
    path("", TodoappList.as_view(), name="list"),
    path("detail/<int:pk>", TodoappDetail.as_view(), name="detail"),
]