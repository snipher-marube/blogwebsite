from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    return render(request, 'blogapp/home.html', context)

def post_detail(request, category_slug, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, publish__year=year, publish__month=month, publish__day=day, category__slug=category_slug, status='published')
    context = {
        'post': post
    }
    return render(request, 'blogapp/post_detail.html', context)

def post_by_category(request):
    context = {}
    return render(request, 'blogapp/post_by_category.html', context)

