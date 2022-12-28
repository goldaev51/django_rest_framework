from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    pubdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}, id({self.pk})'

    class Meta:
        ordering = ['pubdate']


class Comment(models.Model):
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=False, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    pubdate = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['pubdate']
