from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view()),
    path('logout/', login_required(views.LogoutView.as_view(), redirect_field_name=None)),
    path('', include('api.urls')),
    path('', RedirectView.as_view(url="/news")),
]
