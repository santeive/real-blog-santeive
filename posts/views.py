from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def index(request):
    return render(request, "core/home.html")


def post_list(request, tag_slug=None):
    posts = Post.published.all()
    return render(request, 'posts/home.html', {'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    
    return render(request, 'posts/detail.html', {'post':post})