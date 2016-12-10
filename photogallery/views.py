from django.views import generic
from posts.models import Post
from posts.helpers import get_posts


class Home(generic.ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return get_posts(self.request.user, wall=True)

