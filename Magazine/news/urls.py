from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (NewsList, DetailNews, NewsFilterList, PostUpdate, PostCreate, PostDelete, ArticleCreate, upgrade_me,
                    subscribe, CategoryDetail)

urlpatterns = [
   path('', cache_page(60)(NewsList.as_view()), name='posts_list'),
   path('<int:pk>',cache_page(30)(DetailNews.as_view()), name="new_detail"),
   path('search/', NewsFilterList.as_view(), name="filter"),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create', ArticleCreate.as_view(), name='article_create'),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('subscribe/<int:pk>/', subscribe, name='subscribe'),
   path('categories/<int:pk>/', CategoryDetail.as_view(), name='CategoryDetail'),
]
