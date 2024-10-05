from django.contrib import admin
from .models import News, Category
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'published_date', 'created_at', 'updated_at', 'status']
    search_fields = ['title', 'content']
    list_filter = ['status', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 10
    list_editable = ['status', 'content']
    prepopulated_fields = {'slug': ('title',)}
