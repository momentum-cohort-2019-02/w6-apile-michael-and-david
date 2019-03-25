from django import forms
from .models import Comment, Post, Tag
from django.db.models import Count

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', 'replying_to')

class SortForm(forms.Form):
    sorter = forms.ChoiceField(
        label="Sort by",
        choices=[
            ("liked_by", "Likes"),
            ("date_added", "Date Added"),
        ],
        required=False)

    def sort(self, posts):
        if not self.is_valid():
            return None

        data = self.cleaned_data

        if not data['sorter']:
            data['sorter'] = 'date_added'

        elif data['sorter'] == 'liked_by':
            posts = posts.annotate(likes=Count('liked_by')).order_by('-likes', '-date_added')

        else:
            posts = posts.annotate(likes=Count('liked_by')).order_by('-date_added', '-likes')

        return posts
 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'url', 'description', 'audio']




        

        

    