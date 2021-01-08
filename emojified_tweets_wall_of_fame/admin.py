from django.contrib import admin

from .models import Tweet, CustomUser

admin.site.register(CustomUser)
admin.site.register(Tweet)
