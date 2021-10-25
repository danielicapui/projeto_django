from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from polls.utills import selectChoice
from .models import Choice, Question
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)
def detail(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return selectChoice(question)
def raizes(request,a,b,c):
    a,b,c=float(a),float(b),float(c)
    x1=(-b+((b*b-4*a*c)**0.5))/2*a
    x2=(-b-((b*b-4*a*c)**0.5))/2*a
    return HttpResponse("O resultado da equação ({})x^2+({})x+({}) são ({},{})".format(a,b,c,x1,x2))