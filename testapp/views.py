from django.shortcuts import render

def benutzer_list(request):
    return render(request, 'testapp/benutzer_list.html', {})

# Create your views here.
