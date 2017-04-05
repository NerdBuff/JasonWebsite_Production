from django.shortcuts import render
from .models import Post
# Create your views here.

def blog(request):

    posts = Post.objects.exclude(createdDate__isnull=True)

    context = {
        'posts': posts,
        'name' : 'test',
    }

    return render (request, "blog.html", context)
