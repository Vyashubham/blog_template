from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class VyasProfile(models.Model):

    Title = models.CharField(max_length=100)
    Description = HTMLField()
    Date_started = models.DateField()
    Date_ended = models.DateField(null=True)
    Category = models.CharField(max_length=50)
    
    

    def __str__(self):
        return f'{self.Title}'
