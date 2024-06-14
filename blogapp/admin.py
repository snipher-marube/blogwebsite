from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    list_filter = ['created']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f'<img src={obj.image.url} width="100" style="border-radius: 10px;" />')
    
    list_display = ['thumbnail', 'title', 'category', 'status', 'publish', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at', 'publish', 'category']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['-publish', '-created_at']
    autocomplete_fields = ['category']
    raw_id_fields = ['category']
    list_display_links = ['title']

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'body', 'image')
        }),
        ('Publication', {
            'fields': ('publish', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    readonly_fields = ['created_at', 'updated_at']



