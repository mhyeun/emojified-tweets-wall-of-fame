from django.shortcuts import render
from django.http import HttpResponse
import json


def index(response):
    return render(response, "emojified_tweets_wall_of_fame/base.html", {})


def health(response):
    success_message = {"success": True}
    return render(response, "emojified_tweets_wall_of_fame/login.html", {})
