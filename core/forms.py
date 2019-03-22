from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'liked_by', 'tags', 'date_added', 'slug']
        