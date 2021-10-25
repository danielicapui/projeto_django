from django.contrib import admin
from .models import Choice, Question
#melhora a interface da pagina de administração
class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3
#uma classe de campo para mostragem e incremento das tabelas
class QuestionAdmin(admin.ModelAdmin):
    #diz e o que exibir no admin
    list_display = ['pub_date','question_text','was_published_recently']
    #adiciona a capacidade de filtragem por data
    list_filter = ['pub_date']
    #adicion a capacidade de busca por questão texto
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
#regitrando questões
admin.site.register(Question, QuestionAdmin)