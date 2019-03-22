from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):

    text = models.TextField(max_length=500, null=True)

    author = models.ForeignKey(to=User, related_name="comments", default="Anonymous", on_delete=models.SET_DEFAULT)

    date_added = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    liked_by = models.ManyToManyField(to=User, related_name="liked_comments", blank=True)

    replying_to = models.ForeignKey(to=User, related_name="comment_reply", default="Anonymous", on_delete=models.SET_DEFAULT)

    commenting_on = models.ForeignKey(to='Post', related_name="comments", on_delete=models.CASCADE)
    def __str__(self):
        return self.author.username

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

    class Meta:
        ordering = ['-date_added']

    # Relational attributes
    author = models.ForeignKey(
        to=User, 
        default="Anonymous", 
        on_delete=models.SET_DEFAULT, 
        related_name='authored_posts')
    liked_by = models.ManyToManyField(to=User, related_name='liked_posts', blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='posts', blank=True)

    # Content info
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True, blank=True) 
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    #Media fields
    audio = models.FileField(upload_to='audio_clips', blank=True)

    # Utility methods
    def __str__(self):
        return self.title

    def blank_url(self):
        return f"posts/{self.slug}/"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)[:45]
        if not self.url:
            self.url = f"{reverse('index')}{self.slug}/"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.slug})
    