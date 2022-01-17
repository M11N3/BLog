from django.views.generic import ListView

from .models import Article, Blog


class BlogsView(ListView):
    model = Blog
    context_object_name = 'object_list'
    template_name = 'api/blog_list.html'

    def get_queryset(self):
        queryset = self.model.objects.select_related('author').exclude(author=self.request.user.id)
        queryset = queryset.annotate_with_is_subscribed_by_user(self.request.user)
        return queryset


class ArticlesView(ListView):
    model = Article
    template_name = "api/article_list.html"
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = self.model.objects.filter(blog__subscribers=self.request.user.id)
        queryset = queryset.annotate_with_has_read_by_user(self.request.user).order_by('-created_on')
        return queryset
