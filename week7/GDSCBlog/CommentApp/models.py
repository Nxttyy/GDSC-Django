from django.db import models
from BlogApp.models import Post
# Create your models here.

class Comment(models.Model):
    Content = models.TextField()
    Author = models.CharField(max_length = 150)
    publishedDate =  models.DateTimeField()
    Post = models.ForeignKey(Post, on_delete = models.CASCADE)
