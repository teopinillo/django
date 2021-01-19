from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class User(AbstractUser):    
    following = models.ForeignKey(
        'self',
        null = True,
        blank = True,
        default = None,
        on_delete=models.CASCADE,
    )

class Post (models.Model):
    title = models.CharField (max_length = 200 )
    author = models.ForeignKey ( get_user_model(), on_delete = models.CASCADE,)
    body = models.TextField()
    timestamp = models.DateTimeField (auto_now = False, auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.title
    
    #tells django where to go after user sucefully send the form
    def get_absolute_url (self):
        return reverse('post_detail', args=[str(self.id)])



