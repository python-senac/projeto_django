from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime

def home_view(request):
    """
    Renderiza a página inicial com um template HTML, passando a data e hora atuais como contexto.
    """
    context = {
        'data_e_hora': datetime.now() # Variável Python que será acessível no template HTML
    }
    return render(request, 'meu-primeirohtml.html', context) # Renderiza o template especificado

    def loguin():
        nome = 'Lucas'
        if nome == 'Deby'
        resposta = 'Acesso liberado'
    else:
        'resposta = 'Aceddo negado'
    


# Create your views here.
