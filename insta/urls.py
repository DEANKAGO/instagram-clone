from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpattern = [
  path('', views.PostListView, name = 'post_list' )
]