from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def home(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    return render(request, 'blogapp/home.html', context)

def post_detail(request, category_slug, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, publish__year=year, publish__month=month, publish__day=day, category__slug=category_slug, status='published')
    # get all posts in that category as same as this post
    # exclude the current post
    post_category = post.category
    related_posts = Post.published.filter(category=post_category).exclude(id=post.id)
    
    context = {
        'post': post,
        'related_posts': related_posts
    }
    return render(request, 'blogapp/post_detail.html', context)

def posts_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.published.filter(category=category)
        
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blogapp/post_by_category.html', context)

