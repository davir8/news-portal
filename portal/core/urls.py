from django.conf.urls import include, url

urlpatterns = [
    url(r'^noticias$', 'portal.core.views.index', name='index'),
    url(r'^$', 'portal.core.views.store', name='store')
]
