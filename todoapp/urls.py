from unicodedata import name
from django.urls import path
from .views import TodoappCreate, TodoappDelete, TodoappDetail, TodoappList, TodoappUpdate

urlpatterns = [
    path("", TodoappList.as_view(), name="list"),
    path("detail/<int:pk>", TodoappDetail.as_view(), name="detail"),
    path("create/", TodoappCreate.as_view(), name="create"),
    path("update/<int:pk>", TodoappUpdate.as_view(), name="update"),
    path("delete/<int:pk>", TodoappDelete.as_view(), name="delete"),
]