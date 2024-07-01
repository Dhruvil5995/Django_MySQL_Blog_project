from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'date_posted')
    list_filter = ('status', 'date_posted')
    search_fields = ('title', 'content')
