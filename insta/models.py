from django.db import models
from django.utils import timezone
from datetime import datetime
from django.conf import settings 
from django.urls import reverse

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  image = models.ImageField( upload_to='media', null=False, blank=False)
  description = models.TextField()
  date_created = models.DateTimeField(default=timezone.now)
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')

  def save_post(self):
        self.save()
    
  def delete_post(self): 
      self.delete()

  def __str__(self):
    return self.description