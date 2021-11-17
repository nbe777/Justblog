from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Profile')
    profilepic = models.ImageField(upload_to='profilepic')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
