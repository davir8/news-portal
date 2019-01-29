from django.shortcuts import render
from .models import Notice
from .forms import SearchNotice
# Imports redirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def index(request):
    notices = Notice.objects.all()
    template_name = 'home.html'
    msg = ''
    # Verificando se o form foi submetido
    if request.method == 'GET':
        form = SearchNotice(request.GET)
        if form.is_valid():
            notices = Notice.objects.search(form.cleaned_data['title'])
            # Verificando se achou alguma notifica
            if len(notices) == 0:
                msg = "Nenhuma notícia encontrada."
            # Limpando o form
            form = SearchNotice()
    else:
        # Limpando o form
        form = SearchNotice()
    # Passando as variáveis para o contexto
    context = {
        'notices': notices,
        'form': form,
        'msg': msg
    }
    return render(request, template_name, context)
