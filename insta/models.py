from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  image = models.ImageField(blank=True, null=True)
  description = models.TextField()
  date_created = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.description