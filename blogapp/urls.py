from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>/<slug:slug>/<int:year>/<int:month>/<int:day>/', views.post_detail, name='detail'),
    path('category/<slug:slug>/', views.posts_by_category, name='posts_by_category'),
    path('search/', views.post_search, name='post_search'),
]