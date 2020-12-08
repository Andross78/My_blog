from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class User(AbstractUser):
    email = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='posts/', blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment by {self.user}'