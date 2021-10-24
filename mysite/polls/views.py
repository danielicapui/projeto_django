from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Bem vindo. Você está no index da polls!")
