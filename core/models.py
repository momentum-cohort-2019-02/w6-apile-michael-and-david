from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

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
    