from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Comment(models.Model):

    text = models.Charfield(max_length=500), null=True)

    author = models.ForeignKey(to=User, related_name="comments", default="Anonymous", on_delete=models.SET_DEFAULT)

    date_added = models.DateTimeField(null=True, blank=True)

    liked_by = models.ManyToMany(to=User, related_name="liked_comments")

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
    
