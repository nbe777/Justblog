from django.db import models
from django.contrib.auth.models import User
import numpy as np

class BlogModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    blog_content = models.TextField()
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    name = models.CharField(max_length=100)
    comment = models.TextField()
    blog = models.ForeignKey('BlogModel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
