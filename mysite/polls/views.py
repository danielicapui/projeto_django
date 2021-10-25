from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from polls.utills import selectChoice
from .models import Choice, Question
from django.views import generic
from django.utils import timezone
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        #retorna os últimos 5 resultados publicados
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model=Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Exclupi qualquer questão que não foi publicada ainda.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'
def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return selectChoice(request,question)
def raizes(request,a,b,c):
    a,b,c=float(a),float(b),float(c)
    x1=(-b+((b*b-4*a*c)**0.5))/2*a
    x2=(-b-((b*b-4*a*c)**0.5))/2*a
    return HttpResponse("O resultado da equação ({})x^2+({})x+({}) são ({},{})".format(a,b,c,x1,x2))