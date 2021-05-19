from django.db import models


# Create your models here.

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
