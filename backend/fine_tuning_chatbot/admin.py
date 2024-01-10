from django.contrib import admin
from .models import FineTunedModel, TrainingData

# Register your models here.

# 모델을 위한 관리자 인터페이스
# 관리자 인터페이스 등록
# 관리자 인터페이스에서의 표시 필드, 검색 필드, 필터를 지정
@admin.register(FineTunedModel)
class FineTunedModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'base_model')
    search_fields = ('model_name', 'base_model')
    
    
@admin.register(TrainingData)
class TrainingDataAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'completion', 'fine_tuned_model', 'is_fine_tuned', 'will_be_fine_tuned')
    search_fields = ('prompt', 'completion', 'fine_tuned_model__model_name')
    list_filter = ('fine_tuned_model', 'is_fine_tuned', 'will_be_fine_tuned')
