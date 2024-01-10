from django.db import models

# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=250)
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now = True)

    

    def __str__(self) -> str:
        return self.content
    