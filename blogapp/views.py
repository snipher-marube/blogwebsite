from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_elasticsearch_dsl.search import Search

from .models import Post, Category
from .forms import SearchForm

# Create your views here.
def home(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
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

def post_search(request):
    form = SearchForm()
    query = None
    post_results = []
    
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            post_search = Search(index='posts').query('multi_match', query=query, fields=['title', 'body'])
            
            post_search_results = post_search.execute()
            
            post_ids = [hit.meta.id for hit in post_search_results]
         
            post_results = Post.objects.filter(id__in=post_ids)
            
            
    
    
    context = {
        'form': form,
        'query': query,
        'results': post_results,
    }
    
    return render(request, 'blogapp/search.html', context)

