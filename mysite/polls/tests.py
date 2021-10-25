import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse
polls_index='polls:index'
def create_question(question_text, days):
    """
    Cria uma questão com dado texto e com data de publicação por dias
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

"""Boas praticas de test:
    #um “TestClass” separado para cada modelo ou view.
    #um método de teste separado para cada conjunto de condições que você quer testar.
    #nomes de métodos de teste que descrevem a sua função.
"""
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        Se não tem questão para mostrar, mostre alguma coisa
        """
        response = self.client.get(reverse(polls_index))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nada para ver aqui.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questões com data de publicação no passado que são mostrada no index page.
        """
        question = create_question(question_text="Questao no passado.", days=-30)
        response = self.client.get(reverse(polls_index))
        self.assertQuerysetEqual(response.context['latest_question_list'],[question],)

    def test_future_question(self):
        """
        Questões com data de publicação no futuro que não são mostrada no index page.
        """
        create_question(question_text="Questao no futuro.", days=30)
        response = self.client.get(reverse(polls_index))
        self.assertContains(response, "Nada para ver aqui.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Questao no passado.", days=-30)
        create_question(question_text="Questao no futuro.", days=30)
        response = self.client.get(reverse(polls_index))
        self.assertQuerysetEqual(response.context['latest_question_list'],[question],)

    def test_two_past_questions(self):
        """
        verifica 2 questões passadas
        """
        question1 = create_question(question_text="Questao no passado.", days=-30)
        question2 = create_question(question_text="Questao no passado.", days=-5)
        response = self.client.get(reverse(polls_index))
        self.assertQuerysetEqual(response.context['latest_question_list'],[question2, question1],)
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        As informações da view de uma questão com data de publicação no futuro
        retorna um 404 not found.
        """
        future_question = create_question(question_text='Questao no futuro.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        As informações da view de uma questão com data de publicação no passado
        mostra o texto da questão.
        """
        past_question = create_question(question_text='Questao no passado.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)