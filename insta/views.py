from django.shortcuts import render
from .models import *
from django.views.generic import (ListView)

# Create your views here.

class PostListView(ListView):
  template_name = 'main/post_list.html'
  queryset = Post.objects.all()
  context_object_name = 'posts'


