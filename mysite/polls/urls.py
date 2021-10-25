from django.urls import path
from . import views
app_name ='polls'
urlpatterns = [
    #end:localhost/polls/
    path('', views.IndexView.as_view(), name='index'),
    #end:/polls/5/
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    #end:/polls/5/results/
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    #end:/polls/5/vote/
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('<int:a>/<int:b>/<int:c>/raizes/',views.raizes,name='raizes'),
]
