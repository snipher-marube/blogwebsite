from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.post_detail, name='detail'),
    path('category/', views.post_by_category, name='category'),
]