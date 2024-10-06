from django.shortcuts import render, get_object_or_404
from .models import News, Category

# Create your views here.



# filter manager bilan
# def news_list(request):
#     news_listt = News.published.all()
#     context = {'news': news_listt}
#     return render(request, "news/news_list.html", context)


def news_list(request):
    news_listt = News.objects.all()
    context = {'news': news_listt}
    return render(request, "news/news_list.html", context)


def news_detail(request, news_id):
    news_detail = get_object_or_404(News, pk=news_id) #buyerga detailni ushlab olish uchun vergul qoyib shartlar kiritaversa boladi
    context = {'news': news_detail}
    return render(request, "news/news_detail.html", context)


def rokuro(request):
    return render(request, "news/rokuro.html", {})

def sudzuki(request):
    return render(request, "news/sudzuki.html", {})

def home_page(request):
    news = News.published.all()
    categories = Category.objects.all()

    context = {'news': news, 'categories': categories}
    return render(request, "news/index.html", context)

def contact(request):
    return render(request, "news/contact.html" )
