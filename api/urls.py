from django.urls import path

from .views import ArticlesView, ArticleCreateView, ArticlesDetailView, BlogsView, MyArticlesList, MarkAsReadAPI


urlpatterns = [
    path('article/<int:pk>/', ArticlesDetailView.as_view()),
    path('article/create', ArticleCreateView.as_view()),
    path('articles/my', MyArticlesList.as_view()),
    path('article/<int:pk>/markasread', MarkAsReadAPI.as_view()),
    path('blogs', BlogsView.as_view()),
    path('news', ArticlesView.as_view()),
]
