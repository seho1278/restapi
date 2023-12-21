from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer

# Create your tests here.


class ArticleTests(TestCase):
    def setup(self):
        self.client = APIClient()
        self.article_data = {
            'title': 'Test Article',
            'author': 'seho',
            'created_at': '2023-01-01',
        }
        self.article = Article.objects.create(**self.article_data)
        
    def test_get_all_articles(self):
        response = self.client.get('api/v1/articles/')
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data) # check 'result' key
