from django.shortcuts import render
from .models import Notice
from .forms import SearchNotice
# Imports redirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
# Imports webscraping
from bs4 import BeautifulSoup
import requests

def index(request):
    notices = Notice.objects.all()
    template_name = 'home.html'
    msg = ''
    if request.method == 'GET':
        form = SearchNotice(request.GET)
        if form.is_valid():
            notices = Notice.objects.search(form.cleaned_data['title'])
            if len(notices) == 0:
                msg = "Nenhuma notícia encontrada."
            form = SearchNotice()
    else:
        form = SearchNotice()

    context = {
        'notices': notices,
        'form': form,
        'msg': msg
    }
    return render(request, template_name, context)

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
        Notice.objects.get_or_create(title=p1+' '+p2)
    
    return redirect(reverse('core:index'))
