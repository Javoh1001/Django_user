from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'list'


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    model = Post
    fields = ['title', 'author', 'body']


class PostUpdateView(UpdateView):
    template_name = 'post_update.html'
    model = Post
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    model = Post
    success_url = reverse_lazy('home')
