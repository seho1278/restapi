from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 세부모델
class FineTunedModel(models.Model):
    MODEL_CHOICES = [
        ('ada', 'Ada'),
        ('babbage', 'Babbage'),
        ('curie', 'Curie'),
        ('davinci', 'Davinci'),
    ]
    
    model_name = models.CharField(max_length=100)
    base_model = models.CharField(max_length=100, choices=MODEL_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fine_tuned_models', null=True)
    # 파일을 업로드 할 때 OpenAI API가 반환하는 파일 ID를 저장하는 문자 필드
    file_id = models.CharField(max_length=200, null=True, blank=True)
    # 이 필드는 세부 조정 프로세스를 시작할 때 OpenAI API가 반환하는 ID를 저장하는 데 사용
    fine_tune_id = models.CharField(max_length=200, null=True, blank=True)
    # 이 필드는 세부 조정 프로세스가 완료된 후 OpenAI API가 반환하는 세부 조정된 모델의 식별자를 저장하는 데 사용
    fine_tuned_model = models.CharField(max_length=200, null=True, blank=True)
    # 이 필드는 세부 조정 프로세스의 상태를 저장하는 데 사용됩니다. "processing", "complete", "failed" 등과 같은 값을 가질 수 있다.
    status = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.model_name
    

# 세부 모델과 연결된 훈련 데이터
class TrainingData(models.Model):
    fine_tuned_model = models.ForeignKey(FineTunedModel, on_delete=models.CASCADE, related_name='training_data')
    prompt = models.TextField()
    completion = models.TextField()
    # 주어진 훈련 데이터가 모델의 세부 조정에 사용되었는지 여부를 나타내는 부울 필드입니다. 기본값은 False
    is_fine_tuned = models.BooleanField(default=False)
    # 주어진 훈련 데이터가 나중에 모델의 세부 조정에 사용될지 여부를 나타내는 부울 필드입니다. 기본값도 False
    will_be_fine_tuned = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_datas', null=True)

    def __str__(self):
        return f"{self.fine_tuned_model.model_name}의 훈련 데이터"
