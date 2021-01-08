from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Made foreign key relation with no cascade delete since
# we will just replace username with [DELETED]
class Tweet(models.Model):
    content = models.CharField(max_length=512)
    votes = models.IntegerField()
    poster = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content

    def getDescription(self):
        return self.content + " with " + self.votes + " votes."


class Comment(models.Model):
    content = models.CharField(max_length=512)
    poster = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    posted_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content


class TweetsToComments(models.Model):
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
