from django.urls import path

from . import views

urlpatterns = [
    path("wall-of-fame", views.wall_of_fame, name="wall_of_fame"),
    path("wall-of-shame", views.wall_of_shame, name="wall_of_shame"),
    path("health", views.health, name="health"),
    path("authentication", views.authentication, name="authentication"),
]