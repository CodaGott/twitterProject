from django.db import models

# Create your models here.
from django.forms import ModelForm


class Post(models.Model):
    body = models.CharField(max_length=200)
    tweet_date = models.DateTimeField(auto_now_add=True)


class TweetForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
