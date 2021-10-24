from django.urls import path
from . import views
app_name ='polls'
urlpatterns = [
    #end:localhost/polls/
    path('', views.index, name='index'),
    #end:/polls/5/
    path('<int:question_id>/',views.detail,name='detail'),
    #end:/polls/5/results/
    path('<int:question_id>/results/',views.results,name='results'),
    #end:/polls/5/vote/
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('<int:a>/<int:b>/<int:c>/raizes/',views.raizes,name='raizes'),
]
