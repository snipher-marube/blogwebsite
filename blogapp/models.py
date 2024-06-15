from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    class PublishManager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status='published')

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='uploads/posts/%Y/%m/%d', blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()  # default manager
    published = PublishManager()  # custom manager

    class Meta:
        ordering = ['-publish']
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
       return reverse('detail', args=[self.category.slug, self.slug, self.publish.year, self.publish.month, self.publish.day])
