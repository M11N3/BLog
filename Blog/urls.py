from django.contrib import admin
from django.urls import path
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view()),
]
