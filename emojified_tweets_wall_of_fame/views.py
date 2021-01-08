from django.shortcuts import render
from django.http import HttpResponse
import json


def main(response):
    return render(response, "emojified_tweets_wall_of_fame/main.html", {})


def health(response):
    success_message = {"success": True}
    return HttpResponse(json.dumps(success_message))


def authentication(response):
    return render(response, "emojified_tweets_wall_of_fame/login.html", {})
