"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token 

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# schema_view = get_schema_view(
#     openapi.Info(
#         title = 'restapi API',
#         default_version = 'v1',
#         description = 'API documentation for restapi',
#         terms_of_service = 'https://www.example.com/terms/',
#         contact = openapi.Contact(email='contact@example.com'),
#         license = openapi.License(name='BSD License'),
#     ),
#     public = True,
#     permission_classes = (permissions.AllowAny,),   
# )

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls'))
    # path('api/v1/', include('fine_tuning_chatbot.urls')),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    # path('api/v1/', include('restapi.urls')),
    # # path('docs/', include('rest_framework_docs.urls')),
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
