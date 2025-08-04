from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    ordering = ['-created_at']
    search_fields = ['title', 'body']
    list_filter = ['created_at']

admin.site.register(Post, PostAdmin)