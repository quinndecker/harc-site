from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'home.html')
def booking(request):
    return render(request, 'booking-templates/book-now.html')



## Blog Stuff ##

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

#info for sitemap#
def Post(request, post_slug=Post.slug):

    item = get_object_or_404(Post, slug=post_slug)

    return render(request,'post_detail.html', {'post': item})
