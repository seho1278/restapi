class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def mark_as_read(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        article.mark_as_read()
        return Response({'status': 'article marked as read'})
    # 사용자 정의 동작 정의
    
    
from django.test import TestCase
from rest_framework.test import APIClient

class UserListViewTest(TestCase):
    def setup(self):
        self.client = APIClient()
        
    def test_get_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)




