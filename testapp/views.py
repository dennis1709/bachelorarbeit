from django.shortcuts import render, get_object_or_404
from .models import Benutzer

def benutzer_list(request):
    benutzers = Benutzer.objects.all()
    return render(request, 'testapp/benutzer_list.html', {'benutzers': benutzers})

def benutzer_detail(request, pk):
    benutzerszwei = get_object_or_404(Benutzer, pk=pk)
    return render(request, 'testapp/benutzer_detail.html', {'benutzerszwei':benutzerszwei})

# Create your views here.
