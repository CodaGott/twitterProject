from django.shortcuts import render

# Create your views here.
from .models import Post


def post_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'post_index.html', context)


def welcome(request):
    return render(request, 'post_index.html')
