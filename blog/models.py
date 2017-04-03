from django.db import models
from django.utils.timezone import now

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    createdDate = models.DateTimeField()
    publishedDate = models.DateTimeField()
    text = models.TextField()
    author = models.CharField(max_length=100)
    #images =
    #Need to figure out how to associate images to blog post
    uid = models.CharField(max_length=100)

    #Return Title
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if (self.text and self.createdDate is None):
            self.createdDate=now()

        super(Post,self).save(*args, **kwargs)
