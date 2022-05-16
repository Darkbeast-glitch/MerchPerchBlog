from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User





# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    badge  = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    img_url = models.URLField(max_length = 200000)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)



    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Post"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = "Comment"

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class AboutUs(models.Model):
    header = models.CharField(max_length=500)
    about_us = models.TextField(max_length=100000)

    class Meta:

        verbose_name_plural = "About Us"

    def __str__(self):
        return self.header
