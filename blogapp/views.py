from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'blogapp/home.html', context)

def post_by_category(request):
    context = {}
    return render(request, 'blogapp/post_by_category.html', context)

def post_detail(request):
    context = {}
    return render(request, 'blogapp/post_detail.html', context)