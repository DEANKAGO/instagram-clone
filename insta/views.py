from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def postListView(request):
  template_name = 'main/post_list.html'
  posts = Post.objects.all()
  context_object_name = 'posts'

  return render(request, 'main/post_list.html', locals())


