from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restapi import views
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('articles/', views.article_list, name='article_list'),
    # path('articles/<int:article_pk>/', views.article_detail, name='article_detail'),
    # path('comments/', views.comment_list, name='comment_list'),
    # path('comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    # path('articles/<int:article_pk>/comments/', views.comment_create, name='comment_create'),
]
