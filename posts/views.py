from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import Postform

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
          # Yes, Save
          form.save()
          
          # Redirect to Home
          return HttpResponseRedirect('/')
          
        else:
          # No, Show Error
          return HttpResponseRedirect(form.error.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'posts.html', 
                  {'posts': posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request, post_id):
  newlike=Post.objects.get(id = post_id)
  newlike.likecount += 1
  newlike.save()
  return HttpResponseRedirect('/')   
                

def edit(request, post_id):
    # If the method is POST
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES, instance=post)
        # If the form is valid
        if form.is_valid():
          # Yes, Save
          form.save()
          
          # Redirect to Home
          return HttpResponseRedirect('/')
          
        else:
          # No, Show Error
          return HttpResponseRedirect(form.error.as_json())



    # Showx
    return render(request, 'edit.html', 
                  {'post': post})