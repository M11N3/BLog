from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, View
from django.utils.decorators import method_decorator

from .models import Article, Blog


@method_decorator(login_required, name="get")
class BlogsView(ListView):
    model = Blog
    context_object_name = 'object_list'
    template_name = 'api/blog_list.html'

    def get_queryset(self):
        queryset = self.model.objects.select_related('author').exclude(author=self.request.user.id)
        queryset = queryset.annotate_with_is_subscribed_by_user(self.request.user)
        return queryset


@method_decorator(login_required, name="get")
class ArticlesView(ListView):
    model = Article
    template_name = "api/article_list.html"
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = self.model.objects.filter(blog__subscribers=self.request.user.id)
        queryset = queryset.annotate_with_has_read_by_user(self.request.user).order_by('-created_on')
        return queryset


@method_decorator(login_required, name="dispatch")
class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'text']
    template_name = "api/article_create.html"

    def form_valid(self, form):
        form.instance.blog = self.request.user.blog
        return super().form_valid(form)


@method_decorator(login_required, name="get")
class ArticlesDetailView(DetailView):
    model = Article
    context_object_name = "article"
    queryset = Article.objects.all()


@method_decorator(login_required, name="get")
class MyArticlesList(ListView):
    model = Article
    template_name = "api/myarticles_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        return self.model.objects.filter(blog_id=self.request.user.blog)


@method_decorator(login_required, name="get")
class MarkAsReadAPI(View):
    """ This API mark article as read"""

    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        article.those_who_have_read.add(request.user)
        return redirect("/news")


@method_decorator(login_required, name="get")
class SubscribeAPI(View):
    def get(self, request, pk):
        blog = Blog.objects.get(id=pk)
        blog.subscribers.add(request.user)
        return redirect("/blogs")


@method_decorator(login_required, name="get")
class UnsubscribeAPI(View):
    def get(self, request, pk):
        blog = Blog.objects.get(id=pk)
        blog.subscribers.remove(request.user)
        return redirect("/blogs")
