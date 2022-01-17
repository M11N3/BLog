from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

from .models import Blog


def create_blog_by_user(sender, instance, created, **kwargs):
    if created:
        Blog.objects.create(author=instance)


post_save.connect(create_blog_by_user, sender=User, dispatch_uid="create_blog_by_user")
