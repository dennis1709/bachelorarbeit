from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.benutzer_list, name='benutzer_list'),
]
