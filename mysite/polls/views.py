from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.http import Http404
# Create your views here.


# 返回urls 里配置的 index的逻辑
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ','.join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# 返回urls 里配置的 detail的逻辑
# v2.0 返回404的逻辑 抛出异常的使用
# v3.0 返回404的逻辑 get_object_or_404函数的使用
def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html',{'quesion': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# 返回urls 里配置的 results的逻辑
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# 返回urls 里配置的 vote的逻辑
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

