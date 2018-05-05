from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dlocate', views.dlocation, name='DrugLocation'),
    url(r'^Dlist', views.index2, name='index2'),
    url(r'^searchmft', views.searchmft, name='searchmft'),
    url(r'^bdrug', views.bdrug,name='banneddrug'),
    url(r'', views.index, name='index'),
    ]