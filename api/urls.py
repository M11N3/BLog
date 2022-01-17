from django.urls import path

from .views import ArticlesView, BlogsView


urlpatterns = [
    path('blogs', BlogsView.as_view()),
    path('news', ArticlesView.as_view()),
]
