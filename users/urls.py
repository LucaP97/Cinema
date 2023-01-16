from django.urls import path
from . import views

urlpatterns = [
    path("users_home/", views.users_home, name="users_home"),
]