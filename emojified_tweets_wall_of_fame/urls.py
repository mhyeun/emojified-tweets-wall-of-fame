from django.urls import path

from . import views

urlpatterns = [
    path("wall-of-fame", views.wall_of_fame, name="wall_of_fame"),
    path("wall-of-shame", views.wall_of_shame, name="wall_of_shame"),
    path("health", views.health, name="health"),
    path("authentication", views.authentication, name="authentication"),
    path("signup", views.signup, name="signup"),
    path("emojify", views.emojify, name="emojify"),
    path("emojifytweets", views.emojifytweets, name="emojifytweets"),
    path("like", views.like, name="like"),
    path("dislike", views.dislike, name="dislike"),
    path("logout", views.handle_logout, name="handle_logout"),
]
