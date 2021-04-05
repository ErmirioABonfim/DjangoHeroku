from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render




def hello(request):
    return render(request,'index.html')


def articles(request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))


def lerDoBanco(nomeInformado):
    varredura = 0
    lst_nomes = [
        {'nome': 'ze', 'idade': 23, 'sexo': 'M'},
        {'nome': 'Luiz', 'idade': 25, 'sexo': 'M'},
        {'nome': 'Ana', 'idade': 67, 'sexo': 'S'},
    ]

    for nome in lst_nomes:
        if nome['nome'] in nomeInformado:
            resposta = ('O nome  ' + str(nome['nome']) + '   Foi encotrado e ele tem  ' + str(nome['idade']))
            return resposta
        else:
            varredura = varredura + 1
            print('varredura', varredura)

        if varredura == 3 and nome['nome'] != nomeInformado:
            return   'O nome '+  str(nomeInformado) + '  não foi encontrado'

def fNome(request, nome):
    return HttpResponse(lerDoBanco(nome))


def fNome2(request, nome2):
    persona = lerDoBanco(nome2)
    return render(request, 'pessoa.html', {'persona': persona})





