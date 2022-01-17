from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    author = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, blank=True, related_name='subscriptions')
