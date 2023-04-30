from django.contrib import admin
from pybo.models import Question


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # 검색필드 subject 추가
    search_fields = ['subject']

# admin 사이트에 Question 모델을 등록 / 제목으로 검색할 수 있도록 설정
admin.site.register(Question, QuestionAdmin)