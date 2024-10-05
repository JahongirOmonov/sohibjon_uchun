from django.urls import path
from .views import news_list, news_detail, rokuro, sudzuki


urlpatterns = [
    path('all/', news_list, name='news_list'),
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('rokuro/', rokuro, name='rokuro'),
    path('sudzuki/', sudzuki, name='sudzuki'),
]