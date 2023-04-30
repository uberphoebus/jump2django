from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from pybo.models import Question
from pybo.forms import QuestionForm, AnswerForm

# Create your views here.
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


@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id) # type: ignore
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context=context)


@login_required(login_url='common:login')
def question_create(request):
    # POST 방식일 때 : 질문 폼 저장하기
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # 임시저장
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    
    # GET 방식일 때 : 질문 등록하기
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context=context)


