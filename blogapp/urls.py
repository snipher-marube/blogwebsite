from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>/<slug:slug>/<int:year>/<int:month>/<int:day>/', views.post_detail, name='detail'),
    path('category/', views.post_by_category, name='category'),
]