from datetime import timezone
from .managers import PublishedManager

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='news/photos/%Y/%m/%d/')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title












