from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save

from .models import Article, Blog


def create_blog_by_user(sender, instance, created, **kwargs):
    if created:
        Blog.objects.create(author=instance)


def send_mail_for_subscribers(sender, instance, created, **kwargs):
    if created and settings.USE_EMAIL_SEND:
        subscribers = instance.blog.subscribers.all().values_list("email", flat=True)
        send_mail(
            'New Article',
            f'У автора @{instance.blog.author} вышла новая статья http://localhost:8000{instance.get_absolute_url()}',
            settings.EMAIL_HOST_USER,
            subscribers,
            fail_silently=False
        )


post_save.connect(create_blog_by_user, sender=User, dispatch_uid="create_blog_by_user")
post_save.connect(send_mail_for_subscribers, sender=Article, dispatch_uid="send_mail_for_subscribers")
