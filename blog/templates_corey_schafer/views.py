from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'templates_corey_schafer/home.html', context)


def about(request):
    return render(request, 'templates_corey_schafer/about.html', {'title': 'About'})


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



