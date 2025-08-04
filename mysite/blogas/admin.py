from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published', 'created_at']
    ordering = ['-created_at']
    search_fields = ['title', 'body']
    list_filter = ['created_at']
    readonly_fields = ['id', 'created_at']
    list_editable = ['title', 'published']

    fieldsets = [
        ("General", {"fields": ("title", "body")}),
        ("Technical", {"fields": ("id", "created_at", 'published')}),
    ]

admin.site.register(Post, PostAdmin)