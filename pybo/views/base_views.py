from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from pybo.models import Question


def index(request):
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    # 순방향 create_date / 역방향 -create_date
    question_list = Question.objects.order_by('-create_date')
    
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(answer__content__icontains=kw) | # 답변 검색
            Q(author__username__icontains=kw) | # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) # 답변 글쓴이 검색
        ).distinct()
    # 페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context=context)


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    # get_object_or_404는 객체가 없는 경우 404 페이지를 리턴
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request=request, template_name='pybo/question_detail.html', context=context)