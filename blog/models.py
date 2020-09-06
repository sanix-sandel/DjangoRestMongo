from django.db import models


class Post(models.Model):
    title=models.CharField(max_length=50, blank=False, default='No title')
    content=models.TextField()
    published=models.BooleanField(default=False)

    