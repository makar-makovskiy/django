from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
       model = Post
       template_name = 'post.html'

# Create your views here.
