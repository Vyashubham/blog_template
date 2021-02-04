from django.db import models
from django.urls import reverse


class Post(models.Model):

    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Last_Modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('post_detail_view', kwargs={'pk': self.pk})