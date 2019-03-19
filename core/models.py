from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):

    text = models.CharField(max_length=500, null=True)

    author = models.ForeignKey(to=User, related_name="comments", default="Anonymous", on_delete=models.SET_DEFAULT)

    date_added = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    liked_by = models.ManyToManyField(to=User, related_name="liked_comments")

    replying_to = models.ForeignKey(to=User, related_name="comment_reply", default="Anonymous", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.author

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("tag_list", kwargs={"slug": self.slug})

class Post(models.Model):
    # Relational attributes
    author = models.ForeignKey(
        to=User, 
        default="Anonymous", 
        on_delete=models.SET_DEFAULT, 
        related_name='authored_posts')
    liked_by = models.ManyToManyField(to=User, related_name='liked_posts')
    tags = models.ManyToManyField(to=Tag, related_name='posts')

    # Content info
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255) 
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    # Utility methods
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile_page', kwargs={"slug": self.slug})
    