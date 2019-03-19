from django.contrib import admin
from .models import Tag, Comment, Post

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmi(admin.ModelAdmin):
    pass
