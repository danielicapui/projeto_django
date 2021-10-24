from django.shortcuts import HttpResponse,render,get_object_or_404
#from django.template import loader
from .models import Question

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #template=loader.get_template('polls/index.html')
    context={'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)
def detail(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
def results(request, question_id):
    return HttpResponse("Você está olhando os resultados da questão {}.".format(question_id))
def vote(request, question_id):
    return HttpResponse("Você está votando na questão {}.".format(question_id))
def raizes(request,a,b,c):
    a,b,c=float(a),float(b),float(c)
    x1=(-b+((b*b-4*a*c)**0.5))/2*a
    x2=(-b-((b*b-4*a*c)**0.5))/2*a
    return HttpResponse("O resultado da equação ({})x^2+({})x+({}) são ({},{})".format(a,b,c,x1,x2))