from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  image = models.ImageField(blank=True, null=True)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  description = models.TextField()
  date_created = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.description