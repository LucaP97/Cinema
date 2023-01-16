# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello_there/", views.hello_there, name="hello_there"),
]


# urlpatterns += staticfiles_urlpatterns()