from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .models import Tweet, CustomUser

import json


def wall_of_fame(request):
    tweets_list = Tweet.objects.all().order_by("-votes")

    tweets = []
    for tweet in tweets_list:
        tweet_dict = {
            "content": tweet.content,
            "votes": tweet.votes,
            "poster_id": tweet.poster,
        }
        if len(tweets) >= 10:
            break
        tweets.append(tweet_dict)

    return render(
        request, "emojified_tweets_wall_of_fame/wall_of_fame.html", {"tweets": tweets}
    )


def wall_of_shame(request):
    tweets_list = Tweet.objects.all().order_by("votes")

    tweets = []
    for tweet in tweets_list:
        tweet_dict = {
            "content": tweet.content,
            "votes": tweet.votes,
            "poster_id": tweet.poster,
        }
        if len(tweets) >= 10:
            break
        tweets.append(tweet_dict)

    return render(
        request, "emojified_tweets_wall_of_fame/wall_of_shame.html", {"tweets": tweets}
    )


def health(response):
    success_message = {"success": True}
    return HttpResponse(json.dumps(success_message))


def signup(request):
    error = {"error": True, "fields": [], "message": "Something went wrong."}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_retry = request.POST["password_retry"]

        if password != password_retry:
            error["message"] = "Passwords did not match."
            error["fields"].append("password")
            error["fields"].append("password_retry")

            return render(
                request, "emojified_tweets_wall_of_fame/signup.html", {"error": error}
            )

        new_user = CustomUser.objects.create(
            username=username, password=make_password(password)
        )
        new_user.save()
        return redirect("wall_of_fame")

    return render(request, "emojified_tweets_wall_of_fame/signup.html")


def authentication(request):
    error = {"error": True, "fields": [], "message": "Invalid username or password."}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("wall_of_fame")
        else:
            if username == "" and password == "":
                error["message"] = "Username and password cannot be empty."
                error["fields"].append("username")
                error["fields"].append("password")

            elif username == "":
                error["message"] = "Username cannot be empty."
                error["fields"].append("username")

            elif password == "":
                error["message"] = "Password cannot be empty."
                error["fields"].append("password")

            return render(
                request,
                "emojified_tweets_wall_of_fame/authentication.html",
                {"error": error},
            )

    return render(request, "emojified_tweets_wall_of_fame/authentication.html")


def emojify(request):
    return render(request, "emojified_tweets_wall_of_fame/emojify.html")


def emojifytweets(request):
    return render(request, "emojified_tweets_wall_of_fame/emojifytweets.html")
