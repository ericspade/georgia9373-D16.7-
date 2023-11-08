from django.urls import path
from .views import NewsList, ArticlesList, NewsDetail, ArticlesDetail, NewsCreate, ArticleCreate, NewsUpdate, \
    ArticleUpdate, NewsDelete, ArticleDelete, subscribe, CommentView

urlpatterns = [
    path('articles/', ArticlesList.as_view(), name='news'),
    path('articles/<int:pk>', ArticlesDetail.as_view(), name='news'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('articles/subscribe/', subscribe, name='subscribe'),
    path('articles/<int:pk>/comments', CommentView.as_view(), name='add_comment'),
]
