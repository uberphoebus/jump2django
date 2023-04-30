from django.urls import path
from pybo import views

# 네임스페이스 정의
app_name = 'pybo'

urlpatterns = [
    # path(url,view, url alias)
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create')
]