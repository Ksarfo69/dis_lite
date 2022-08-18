from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home Page"),
    path('rooms/', views.rooms, name="Rooms Page")
]