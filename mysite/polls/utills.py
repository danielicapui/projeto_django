from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Choice, Question

def selectChoice(request,question):
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # mostrar o form atualizado
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Você não escolheu uma opção!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # sempre retorna um HttpResponseRedirect depois de lidar com a solicitação
        #previne envio repetido, caso o usuario retorne.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))