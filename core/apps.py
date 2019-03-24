from django.apps import AppConfig
import django_filters
from .models import Post

class CoreConfig(AppConfig):
    name = 'core'

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['author', 'liked_by', 'tags', ]

