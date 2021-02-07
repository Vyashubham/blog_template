from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.utils.text import slugify


class Post(models.Model):

    Title = models.CharField(max_length=100)
    Content = HTMLField()
    Date = models.DateTimeField(auto_now_add=True)
    Last_Modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('post_detail_view', kwargs={'slug': self.slug})