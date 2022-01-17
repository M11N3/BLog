from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save, m2m_changed

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


def remove_has_read_articles_after_unsubscribe(sender, instance, pk_set, action, **kwargs):
    if action == "pre_remove":
        for user_id in pk_set:
            article = instance.article_set.all()
            user = User.objects.get(id=user_id)
            user.read_articles.remove(*article)


post_save.connect(create_blog_by_user, sender=User, dispatch_uid="create_blog_by_user")
post_save.connect(send_mail_for_subscribers, sender=Article, dispatch_uid="send_mail_for_subscribers")
m2m_changed.connect(
    remove_has_read_articles_after_unsubscribe,
    sender=Blog.subscribers.through,
    dispatch_uid="remove_has_read_articles_after_unsubscribe"
)
