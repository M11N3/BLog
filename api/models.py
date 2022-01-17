from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    author = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, blank=True, related_name='subscriptions')


class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    those_who_have_read = models.ManyToManyField(User, blank=True, related_name='read_articles')

    def get_absolute_url(self):
        return f"/article/{self.pk}"

