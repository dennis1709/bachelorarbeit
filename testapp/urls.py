from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('', views.benutzer_list, name='benutzer_list'),
    url(r'^benutzer/(?P<pk>\d+)/$', views.benutzer_detail, name='benutzer_detail'),

]
