from django.urls import path
from . import views # importez views.py folderul curent

urlpatterns = [
    path("login", views.login, name = "login"),
    path("weather", views.weather, name = "weather"),
    path("nasa", views.nasa, name = "nasa")
]