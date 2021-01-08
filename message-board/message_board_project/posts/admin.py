from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ('comment',)

admin.site.register (Post, PostAdmin)

