from django.contrib.auth.models import User
from django.db import models
from django.db.models import Case, When, BooleanField


class ArticleQuerySet(models.QuerySet):
    def annotate_with_has_read_by_user(self, current_user, *args, **kwargs):
        read_articles = current_user.read_articles.values("id")
        return self.annotate(has_read=Case(When(id__in=read_articles, then=True),
                                           default=False,
                                           output_field=BooleanField()))


class BlogQuerySet(models.QuerySet):
    def annotate_with_is_subscribed_by_user(self, current_user, *args, **kwargs):
        subscriptions = current_user.subscriptions.values("id")
        return self.annotate(is_subscribed=Case(When(id__in=subscriptions, then=True),
                                                default=False,
                                                output_field=BooleanField()))


class Blog(models.Model):
    author = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, blank=True, related_name='subscriptions')

    objects = BlogQuerySet.as_manager()


class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    those_who_have_read = models.ManyToManyField(User, blank=True, related_name='read_articles')

    objects = ArticleQuerySet.as_manager()

    def get_absolute_url(self):
        return f"/article/{self.pk}"

