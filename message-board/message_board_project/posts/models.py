from django.db import models

class Post (models.Model):
    date_created = models.DateTimeField (auto_now_add=True, null=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment[:50]

