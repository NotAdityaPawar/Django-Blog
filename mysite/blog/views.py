from django.shortcuts import render
from django.views import generic
from .models import Post

class PostListView(generic.ListView):
    model = Post
    template_name = "post_list.html"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(generic.CreateView):
    model  = Post
    template_name = "add_post.html"
    fields = "__all__"