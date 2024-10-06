from django.urls import path
from .views import news_list, news_detail, rokuro, sudzuki, home_page, contact


urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
    path('rokuro/', rokuro, name='rokuro'),
    path('sudzuki/', sudzuki, name='sudzuki'),

    path('', home_page, name='home_page'),

    path('contact/', contact, name='contact'),
]