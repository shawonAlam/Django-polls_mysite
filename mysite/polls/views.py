from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404

from .models import Question

####### this is my code


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_qs_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not found")
    return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    response = "You're looking at the result of the question $s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Yo're voting on the question $s." % question_id)


