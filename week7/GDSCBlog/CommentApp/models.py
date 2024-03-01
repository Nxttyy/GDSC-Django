from django.db import models
from BlogApp.models import Post
from django.utils import timezone
# Create your models here.

class Comment(models.Model):
    Content = models.TextField()
    Author = models.CharField(max_length = 150)
    publishedDate =  models.DateTimeField(default = timezone.now)
    Post = models.ForeignKey(Post, on_delete = models.CASCADE)
