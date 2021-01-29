from django.db import models

class Post(models.Model):

    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Last_Modified = models.DateTimeField(auto_now=True)
