from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 사용자 정의 인증 로직 구현
        
        # 헤더 추출
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            # 헤더가 없으면 None을 반환하고 다음 인증 클래스로 이동
            return None

        # 헤더가 있는 경우, "Bearer 토큰" 형식으로 되어 있으므로 토큰 추출
        try:
            token = auth_header.split()[1]
        except IndexError:
            # 토큰이 없는 경우
            raise AuthenticationFailed('토큰이 유효하지 않습니다.')

        # 토큰을 사용하여 사용자 인증
        user = self.authenticate_user_with_token(token)
        
        if user is None:
            # 사용자 인증 실패
            raise AuthenticationFailed('토큰이 유효하지 않습니다.')
        
        # 인증에 성공한 경우, (user, auth) 형태의 튜플 반환
        return (user, None)
    
    
    def authenticate_user_with_token(self, token):
        try:
            # 토큰을 사용하여 사용자를 인증
            user = User.objects.get(auth_token__key=token)
        except User.DoesNotExist:
            # 사용자가 존재하지 않는 경우
            return None

        # 사용자 객체 반환
        return user
