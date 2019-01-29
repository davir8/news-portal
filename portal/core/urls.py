from django.conf.urls import include, url

urlpatterns = [
    # URL para buscar as noticias do banco de dados
    url(r'^noticias$', 'portal.core.views.index', name='index'),
    # URL para salvar as noticias no banco de dados
    url(r'^$', 'portal.core.views.store', name='store')
]
