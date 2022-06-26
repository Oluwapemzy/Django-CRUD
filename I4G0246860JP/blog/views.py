from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic.

from I4G0246860JP.blog.models import Post

# Create your views here.
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView)