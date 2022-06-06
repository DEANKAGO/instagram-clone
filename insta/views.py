from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


from .models import *
from .forms import UploadForm, CreateUserForm

# Create your views here.

def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		
	return render(request, 'main/register.html', locals())



def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('post_list')
		else:
			messages.info(request, 'Username OR password is incorrect')

	return render(request, 'main/login.html', locals())


def logoutUser(request):
	logout(request)
	return redirect('login')




def postListView(request):
  template_name = 'main/post_list.html'
  posts = Post.objects.all()
  context_object_name = 'posts'

  return render(request, 'main/post_list.html', locals())

def postCreateView(request):
  user = request.user
  form = UploadForm(instance=user)

  if request.method == 'POST':
    form = UploadForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
      form.save()
  return render(request, 'main/post_create.html', locals())


    
  
      
  


