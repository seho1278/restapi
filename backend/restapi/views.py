from rest_framework import status, viewsets
from rest_framework.views import APIView, exception_handler
from rest_framework.decorators import api_view, permission_classes, action

from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.throttling import UserRateThrottle
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from .models import Article, Comment, Author
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, UserSerializer


# Create your views here.

# class ArticleListView(ListAPIView):
#     # ListAPIView를 상속받은 ArticleListView 정의
#     articles = Article.objects.all()
#     serializer = ArticleListSerializer
#     # 쿼리셋과 시리얼라이저 지정
    
    
class ArticleViewSet(viewsets.ModelViewSet):
    # viewsets.MoodelViewSet을 상속받을 클래스 정의
    # .list(), .create(), .retrieve(), .update(), .destroy() 동작 포함
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    basename = 'articles'
    
    # 해당 뷰셋의 모든 액션에 대해 인증된 사용자만이 접근할 수 있도록 설정
    permission_classes = [IsAuthenticated]
    
    # 뷰셋에 사용자 정의 동작 추가
    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        article = self.get_object()
        article.mark_as_read()
        return Response({'status': 'article marked as read'})
    # mark_as_read 메소드 정의 action 데코레이터로 장식
    # 동작이 개별 article 인스턴스(detail)를 대상으로 하며 POST 요청에 응답해야 함을 의미
    
    # CRUD 기능
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class UserRegistrationView(CreateAPIView):
    serializer_class = UserSerializer
    

class UserLoginView(GenericAPIView):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            
            refresh = RefreshToken.for_user(user)
            response = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response)
        



# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def article_list(request):
#     if request.method == 'GET':
#         # 게시글 목록 조회
#         articles = Article.objects.all()
#         # 직렬화(다중 객체는 many=True 설정)
#         serializer = ArticleListSerializer(articles, many=True)
#         # JSON으로 응답
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         # 사용자 데이터를 받아 직렬화
#         serializer = ArticleSerializer(data=request.data)
#         # 유효성 검사
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # 성공시 201 응답
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # 실패시 400 응답
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'DELETE', 'PUT'])
# def article_detail(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def comment_list(request):
#     if request.method == 'GET':
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)


# @api_view(['GET', 'DELETE', 'PUT'])
# def comment_detail(request, comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     if request.method == 'GET':
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method == 'PUT':
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)                    
    
    
# @api_view(['POST'])
# def comment_create(request, article_pk):
#     # 몇번 게시글에 작성되는지 확인해야함
#     article = Article.objects.get(pk=article_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(article=article) # modelform의 commit=False와 동일
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)
#     if response is not None:
#         custom_data = {'detail': response.data['detail']}
#         response.data = custom_data
#     return response


# class CustomPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100
    

# class ArticleListView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated, IsAdminUser]
#     throttle_classes = [UserRateThrottle]
    
#     pagination_class = CustomPagination
    
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'author']
    
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleListSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
