from django.shortcuts import render, redirect, reverse
from .models import BlogPost
from .forms import BlogForm


def view_blog(request):
    """ A view to show all products """

    posts = BlogPost.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)