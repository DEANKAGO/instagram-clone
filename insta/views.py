from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
		
	 
from .models import *
from .forms import * 
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



@login_required(login_url='/login')
def postListView(request):
	template_name = 'main/post_list.html'
	posts = Post.objects.all()
	context_object_name = 'posts'

	return render(request, 'main/post_list.html', locals())

# @login_required
def postCreateView(request):
    user = request.user
    form = UploadForm(instance=user)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            
            new_post = Post.objects.create(author_id=user.id,
                                image=form.cleaned_data['image'],
                                description=form.cleaned_data['description'])
            return redirect('post_list')
        return redirect('/')
    else:
        return render(request, 'main/post_create.html', {'form': form})

def delete(request, id):
	if request.method == 'POST':
		photo = Post.objects.all()
		photo.delete()
		return redirect('/')



	# user = request.user
	# form = UploadForm(instance=user)

	# if request.method == 'POST':
	# 	form = UploadForm(request.POST, request.FILES, instance=user)
	# 	print("is_valid--->", form.is_valid())
	# 	import pdb
	# 	pdb.set_trace()
	# 	if form.is_valid():
	# 		print("cleaned_data--->", form.cleaned_data)
	# 		form.save()
	# 		return redirect('post_list')
	# context= {'form': form }
	# return render(request, 'main/post_create.html', context)



	# if request.method == 'POST':

	# 	form = UploadForm(request.POST)
	# 	if form.is_valid():
	# 			print('valid')
	# # else:
	# #     form = UploadForm()
	# return render(request, 'main/post_create.html', locals())







def PostDetailView(request):
	# template_name = 'main/details.html'
	# post = get_object_or_404(Post, id=id)

	# return render(request, 'main/details.html', {'post': post})
	# template_name = 'main/details.html'
	# posts = Post.objects.all().filter(date_created__lte=timezone.now())
	# print(posts[0].image)
	# def get_object(self):
	# 		id_ = self.kwargs.get("id")
	# 		print(locals())
	# 		return get_object_or_404(Post, id=id_)
	# posts = Post.objects.filter(id=id)
	return render(request, 'main/details.html', locals())


def PostDeleteView(request):
	template_name = 'main/delete.html'

	def get_object(self):
			id_=self.kwargs.get("id")
			return get_object_or_404(Post, id=id_)

	def get_success_url(self):
			return reverse('post_list')
	return render(request, 'main/delete.html', locals())				
	


def profile(request):
	return render(request, 'main/profile.html', locals())
	
			
	


