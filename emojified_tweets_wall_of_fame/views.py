from django.shortcuts import render
from django.http import HttpResponse
import json


def index(request):
    return HttpResponse("This is the emojified_tweets_wall_of_fame index.")


def health(request):
    success_message = {"success": True}
    return HttpResponse(json.dumps(success_message))
