from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Made foreign key relation with no cascade delete since
# we will just replace username with [DELETED]


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Tweet(models.Model):
    content = models.CharField(max_length=512)
    votes = models.IntegerField()
    poster = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.content

    def getDescription(self):
        return self.content + " with " + self.votes + " votes."
