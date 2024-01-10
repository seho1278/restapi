from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FineTunedModelViewSet,
    TrainingDataViewSet,
    convert_jsonl_file,
    upload_jsonl_file,
    create_finetune,
    retrieve_finetune,
)

# 라우터는 각각의 뷰셋에 대해 표준 액션 (목록, 생성, 조회, 업데이트, 삭제)에 대한 적절한 URL을 자동으로 생성
router = DefaultRouter()
router.register(r'fine_tuned_models', FineTunedModelViewSet)
router.register(r'training_data', TrainingDataViewSet)

openai_patterns = [
    path('convert/<int:finetuned_model_id>/', convert_jsonl_file, name='convert_jsonl_file'),
    path('upload/<int:finetuned_model_id>/', upload_jsonl_file, name='upload_jsonl_file'),
    path('create/<int:finetuned_model_id>/', create_finetune, name='create_finetune'),
    path('retrieve/<int:finetuned_model_id>/', retrieve_finetune, name='retrieve_finetune'),
]

urlpatterns = [
    # path('hello/', views.hello_world),
    # 라우터의 모든 URL을 루트 경로 아래의 urlpatterns에 포함
    path('', include(router.urls)),
    path('openai/', include((openai_patterns, 'openai'))),
]

