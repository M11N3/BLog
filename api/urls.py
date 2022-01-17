from django.urls import path

from .views import ArticlesView, ArticlesDetailView, BlogsView


urlpatterns = [
    path('article/<int:pk>/', ArticlesDetailView.as_view()),
    path('blogs', BlogsView.as_view()),
    path('news', ArticlesView.as_view()),
]
