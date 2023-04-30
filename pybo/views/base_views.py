from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from pybo.models import Question


def index(request):
    page = request.GET.get('page', '1') # 페이지
    # 순방향 create_date / 역방향 -create_date
    question_list = Question.objects.order_by('-create_date')
    # 페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context=context)


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    # get_object_or_404는 객체가 없는 경우 404 페이지를 리턴
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request=request, template_name='pybo/question_detail.html', context=context)