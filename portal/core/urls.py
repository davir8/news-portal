from django.conf.urls import include, url

urlpatterns = [
    # URL para buscar as noticias do banco de dados
    url(r'^$', 'portal.core.views.index', name='index'),
]
