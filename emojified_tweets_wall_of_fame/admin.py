from django.contrib import admin

from .models import Tweet, CustomUser, CustomUserToTweet

admin.site.register(CustomUser)
admin.site.register(Tweet)
admin.site.register(CustomUserToTweet)
