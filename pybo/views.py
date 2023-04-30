from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from pybo.models import Question

# Create your views here.
def index(request):
    # 순방향 create_date / 역방향 -create_date
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request=request, template_name='pybo/question_list.html', context=context)

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    # get_object_or_404는 객체가 없는 경우 404 페이지를 리턴
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request=request, template_name='pybo/question_detail.html', context=context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)