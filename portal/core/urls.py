from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'portal.core.views.index', name='index'),
    url(r'^salvar$', 'portal.core.views.store', name='store'),
]
