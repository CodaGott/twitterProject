from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Post, TweetForm


def post_index(request):
    posts = Post.objects.all().order_by('-tweet_date')
    context = {
        'posts': posts
    }
    return render(request, 'post_index.html', context)


# def welcome(request):
#     return render(request, 'post_index.html')


# def single_post(request, pk):
#     post = Post.objects.get(pk=pk)
#     context = {
#         'post': post
#     }
#     return render(request, 'single_post.html', context)


def home_view(request):
    posts = Post.objects.all().order_by('-tweet_date')
    if request.method == 'POST':
        form = TweetForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = TweetForm()
    return render(request, 'home.html', {'form': form, 'posts': posts})
