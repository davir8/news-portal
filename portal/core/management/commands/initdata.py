from django.core.management.base import BaseCommand, CommandError
from portal.core.models import Notice
# Imports webscraping
from bs4 import BeautifulSoup
import requests

class Command(BaseCommand):
    help = 'Captura noticias tecmundo'

    # Buscar as noticias do tecmundo e salvar no banco de dados
    def handle(self, **options):
        # Fazendo requisição ao site do tecmundo
        html =  requests.get('https://www.tecmundo.com.br/').text
        # Criando objeto usando biblioteca html5
        soup = BeautifulSoup(html, 'html5lib')
        # Buscando as divs do carousel que possui as principais noticias
        data = soup.find_all('div',attrs={'class':'nzn-main-text'})

        # Percorrendo os elementos filhos
        for child in data:
            # Extraindo primeira parte
            p1 = child.find('strong').text
            # Extraindo segunda parte
            p2 = child.find('h2').text
            # Criando um objeto noticia com titulo concatenado
            Notice.objects.get_or_create(title=p1+' '+p2)
        self.stdout.write('Noticias capturadas com sucesso')