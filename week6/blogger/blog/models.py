from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateField(default = timezone.now)
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now = True)

    class meta:
        ordering = ['-publish']

    def __str__(self) -> str:
        return self.title
    