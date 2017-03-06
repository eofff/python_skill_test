from django.conf.urls import url

from . import views

app_name = 'fias'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api_complete_addr$', views.api_complete_addr, name='api_complete_addr'),
]
