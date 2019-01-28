from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'portal.core.views.home', name='home')
]
