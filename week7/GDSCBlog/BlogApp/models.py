from django.db import models
# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length = 250, unique = True)
    Content = models.TextField()
    Category = models.CharField(max_length = 150)
    Image = models.ImageField()
    # Tags = ArrayField(models.CharField)


