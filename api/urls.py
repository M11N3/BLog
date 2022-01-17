from django.urls import path

from .views import ArticlesView, ArticleCreateView, ArticlesDetailView, BlogsView


urlpatterns = [
    path('article/<int:pk>/', ArticlesDetailView.as_view()),
    path('article/create', ArticleCreateView.as_view()),
    path('blogs', BlogsView.as_view()),
    path('news', ArticlesView.as_view()),
]
