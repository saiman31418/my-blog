from . import views
from .views import *
from django.urls import path

urlpatterns=[
    path('register', register, name="register"),
    path('login', login, name="login"),
    path('Post', Post, name="Post"),
    path('delete/<int:id>', delete, name="delete"),
    path("show", show, name="show"),
    path('', home, name="home")

]