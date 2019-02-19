from django.shortcuts import render
from .models import Benutzer

def benutzer_list(request):
    benutzers = Benutzer.objects.all()
    return render(request, 'testapp/benutzer_list.html', {'benutzers': benutzers})

# Create your views here.
