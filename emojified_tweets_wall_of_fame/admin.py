from django.contrib import admin

from .models import User, Tweet, Comment, TweetsToComments

admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(TweetsToComments)
