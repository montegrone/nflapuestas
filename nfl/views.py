from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo
# Create your views here.
def home(req):
#   import pdb; pdb.set_trace()
    equipos=Equipo.objects.all()
    return render(req, 'home.html', {'equipos': equipos})

# def comparar(equipo1,equipo2):
#     import...
#     print(equipo1.valor,equipo2.valor)