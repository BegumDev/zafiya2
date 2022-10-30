from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
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

def read_post(request, id):
    """ View individual post and be able to comment on them"""

    post = BlogPost.objects.get(id=int(id))

    template = 'blog/read_post.html'
    context = {
        'post': post,
    }
    return render(request, template, context)


def create_post(request):
    """ View to create a blog post """

    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid:
            data = form.save(commit=False)
            data.author = User(id=request.user.id)
            data.save()

            messages.success(request, 'Blog post successfully created')
            return redirect(reverse('view_blog'))
        else:
            messages.error(request, 'There was an error with the form. Please try again.')
    else:
        form = BlogForm()
    
    template = 'blog/create_post.html'
    context = {
          'form': form,
      }

    return render(request, template, context)


def update_post(request, id):
    """ View to create a blog post """

    post = BlogPost.objects.get(id=int(id))

    current_info = {
        'blog_title': post.blog_title,
        'content': post.content,
    }
    form = BlogForm(initial=current_info)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            messages.success(request, 'Blog post successfully updated')
            return redirect(reverse('view_blog'))
        else:
            messages.error(request, 'There was an error with the form. Please try again.')
    
    template = 'blog/update_post.html'
    context = {
          'form': form,
      }

    return render(request, template, context)

def delete_post(request, id):
    post = BlogPost.objects.get(id=int(id))
    post.delete()

    return redirect(reverse('view_blog'))