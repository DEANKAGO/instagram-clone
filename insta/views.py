from django.shortcuts import render
from .forms import PostForm
from .models import *
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def postListView(request):
  template_name = 'main/post_list.html'
  posts = Post.objects.all()
  context_object_name = 'posts'

  return render(request, 'main/post_list.html', locals())

def PostCreateView(request):
    template_name = 'main/post_create.html'
    form_class = PostForm
    posts = Post.objects.all()     #.filter(created_date__lte=timezone.now())
    #success_url = '/'
    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user 
        return super().form_valid(form)
      
  


