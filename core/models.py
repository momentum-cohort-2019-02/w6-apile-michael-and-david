from django.db import models

# Create your models here.

class Comment(models.Model):

    text = models.Charfield(max_length=500), null=True)

    author = models.ForeignKey(to=User, related_name="comments", default="Anonymous", on_delete=models.SET_DEFAULT)

    date_added = models.DateTimeField(null=True, blank=True)

    liked_by = models.ManyToMany(to=User, related_name="liked_comments")

    replying_to = models.ForeignKey(to=User, related_name="comment_reply", default="Anonymous", on_delete=models.SET_DEFAULT)


    def __str__(self):
        return self.author