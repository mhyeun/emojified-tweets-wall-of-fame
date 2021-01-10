from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from .models import Tweet, CustomUser, CustomUserToTweet

import requests
import json


def wall_of_fame(request):
    tweets_list = Tweet.objects.all().order_by("-votes")
    tweets = []
    for tweet in tweets_list:
        tweet_dict = {
            "content": tweet.content,
            "votes": tweet.votes,
            "poster_id": tweet.poster,
            "id": tweet.pk,
        }
        if len(tweets) >= 10:
            break
        tweets.append(tweet_dict)

    voted_tweets = []
    if not request.user.is_anonymous:
        custom_user_to_tweets_list = CustomUserToTweet.objects.filter(
            voter=request.user
        )

        for custom_user_to_tweets in custom_user_to_tweets_list:
            tweet_dict = {
                "id": custom_user_to_tweets.tweet.pk,
                "is_upvote": custom_user_to_tweets.is_upvote,
            }
            voted_tweets.append(tweet_dict)

    return render(
        request,
        "emojified_tweets_wall_of_fame/wall_of_fame.html",
        {"tweets": tweets, "voted_tweets": voted_tweets},
    )


def wall_of_shame(request):
    tweets_list = Tweet.objects.all().order_by("votes")

    tweets = []
    for tweet in tweets_list:
        tweet_dict = {
            "content": tweet.content,
            "votes": tweet.votes,
            "poster_id": tweet.poster,
            "id": tweet.pk,
        }
        if len(tweets) >= 10:
            break
        tweets.append(tweet_dict)

    voted_tweets = []
    if not request.user.is_anonymous:
        custom_user_to_tweets_list = CustomUserToTweet.objects.filter(
            voter=request.user
        )

        for custom_user_to_tweets in custom_user_to_tweets_list:
            tweet_dict = {
                "id": custom_user_to_tweets.tweet.pk,
                "is_upvote": custom_user_to_tweets.is_upvote,
            }
            voted_tweets.append(tweet_dict)

    return render(
        request,
        "emojified_tweets_wall_of_fame/wall_of_fame.html",
        {"tweets": tweets, "voted_tweets": voted_tweets},
    )


def health(response):
    success_message = {"success": True}
    return HttpResponse(json.dumps(success_message))


def about(request):
    return render(request, "emojified_tweets_wall_of_fame/about.html")


def signup(request):
    error = {"error": True, "fields": [], "message": "Something went wrong."}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_retry = request.POST["password_retry"]
        email = request.POST["email"]

        if password != password_retry:
            error["message"] = "Passwords did not match."
            error["fields"].append("password")
            error["fields"].append("password_retry")

            return render(
                request, "emojified_tweets_wall_of_fame/signup.html", {"error": error}
            )

        new_user = CustomUser.objects.create(
            username=username, password=make_password(password), email=email
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


@login_required(login_url="/authentication")
def emojify(request):
    TWITTER_API_URL = "http://mhyeun.pythonanywhere.com/emojify-tweets"
    if request.method == "POST":
        twitter_username = request.POST["twitter_username"]
        number_of_tweets = request.POST["number_of_tweets"]

        emojified_tweets = requests.get(
            TWITTER_API_URL,
            params={"username": twitter_username, "tweets": number_of_tweets},
        )

        emojified_tweets_list = json.loads(emojified_tweets.text)

        emojified_tweets_to_add = []
        for emojified_tweets in emojified_tweets_list:
            tweet = Tweet(content=emojified_tweets, votes=0, poster=request.user)
            emojified_tweets_to_add.append(tweet)

        Tweet.objects.bulk_create(emojified_tweets_to_add)

        return render(
            request,
            "emojified_tweets_wall_of_fame/emojifytweets.html",
            {"emojified_tweets": emojified_tweets_list},
        )
    return render(request, "emojified_tweets_wall_of_fame/emojify.html")


@login_required(login_url="/authentication")
def emojifytweets(request):
    return render(request, "emojified_tweets_wall_of_fame/emojifytweets.html")


@login_required(login_url="/authentication")
def like(request):
    if request.method == "POST":
        next = request.POST["next"]
        tweet_id = request.POST["tweet_id"]
        tweet = Tweet.objects.get(id=tweet_id)

        tweet.votes += 1

        relation = CustomUserToTweet.objects.create(
            voter=request.user, tweet=tweet, is_upvote=True
        )
        relation.save()
        tweet.save()

        return HttpResponseRedirect(next)


@login_required(login_url="/authentication")
def dislike(request):
    if request.method == "POST":
        next = request.POST["next"]
        tweet_id = request.POST["tweet_id"]
        tweet = Tweet.objects.get(id=tweet_id)

        tweet.votes -= 1

        relation = CustomUserToTweet.objects.create(
            voter=request.user, tweet=tweet, is_upvote=False
        )
        relation.save()
        tweet.save()

        return HttpResponseRedirect(next)


def handle_logout(request):
    logout(request)
    return render(request, "emojified_tweets_wall_of_fame/authentication.html")
