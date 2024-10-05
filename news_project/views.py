from django.shortcuts import render
from .models import News, Category

# Create your views here.

def news_list(request):
    news_listt = News.objects.all()
    context = {'news': news_listt}
    return render(request, "news/news_list.html", context)

