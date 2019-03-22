from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', 'replying_to')



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'url', 'description', 'audio']
