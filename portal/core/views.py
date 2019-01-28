from django.shortcuts import render
from .models import Notice
from bs4 import BeautifulSoup
import requests

# Retorna a pagina inicial
def home(request):
    return render(request, 'home.html')

# Buscar as noticias do tecmundo e salvar no banco de dados
def store(request):
    # Fazendo requisição ao site do tecmundo
    html =  requests.get('https://www.tecmundo.com.br/').text
    # Criando objeto usando biblioteca html5
    soup = BeautifulSoup(html, 'html5lib')
    # Buscando as divs do carousel que possui as principais noticias
    data = soup.find_all('div',attrs={'class':'nzn-main-text'})
    # Criando array de dados extraidos
    extracted_data = []

    # Percorrendo os elementos filhos
    for child in data:
        # Extraindo primeira parte
        p1 = child.find('strong').text
        # Extraindo segunda parte
        p2 = child.find('h2').text
        # Criando um objeto noticia com titulo concatenado
        Notice.objects.create(title=p1+' '+p2)


def index(request):
    notices = Notice.objects.all()
    template_name = 'home.html'
    context = {
        'notices': notices
    }
    return render(request, template_name, context)