from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home(req):
    if req.method == 'POST' and req.POST['descripcion']:
        todo = Todo(descripcion=req.POST['descripcion'], terminado=False)
        todo.save()
        return HttpResponseRedirect("/")


    todos=Todo.objects.all()
    hechos=[]
    porhacer=[]
    for xx in todos:
        if xx.terminado:
            hechos.insert(0,xx)
        else:
            porhacer.insert(0,xx)



    return render(req, 'home.html', {'hechos': hechos, 'porhacer': porhacer})

# def comparar(equipo1,equipo2):
#     import...
#     print(equipo1.valor,equipo2.valor)

def marcar_como_hecho(req):
    if req.method == 'POST':
        todo = Todo.objects.get(id=req.POST['id'])
        todo.terminado = True
        todo.save()
        return HttpResponseRedirect("/")


