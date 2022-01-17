from django.views.generic import ListView

from .models import Blog


class BlogsView(ListView):
    model = Blog
    context_object_name = 'object_list'
    template_name = 'api/blog_list.html'

    def get_queryset(self):
        queryset = self.model.objects.select_related('author').exclude(author=self.request.user.id)
        queryset = queryset.annotate_with_is_subscribed_by_user(self.request.user)
        return queryset
