from django.shortcuts import render , redirect
from core.models import Filial
from core.forms import FilialForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from perfil.models import Avatar
from django.core.cache import cache


# Create your views here.
@login_required(redirect_field_name='next')
def inicio(request):
    total = cache.get("contador", 0)
    total += 1
    cache.set("contador", total)
    print(f"\n\nCACHE:\n{cache.get('contador')}\n\n")
    try:
        avatar = Avatar.objects.get(user=request.user)
        context = {'imagen': avatar.imagen.url}
    except Avatar.DoesNotExist:
        context = {}

    return render(request, 'core/index.html', context)

@login_required(redirect_field_name='next')
def agregar(request):
    
    if request.method == "POST":
        
        filial_form = FilialForm(request.POST)
        
        if filial_form.is_valid():
            data = filial_form.cleaned_data
            filial = Filial(nombre=data["nombre"], sede=data["sede"])
            filial.save()
            return render(request, 'core/index.html')
        
    filial_form = FilialForm()    
    return render(request, 'core/agregar_filial.html', {"form": filial_form})
@login_required(redirect_field_name='next')
def mostrar(request):
    
    filialesx = Filial.objects.all()

    return render(request, 'core/mostrar_filial.html',{"filiales": filialesx})

def editar(request, id_filial):

    filial = Filial.objects.get(id=id_filial)

    if request.method == "POST":
        filial_form = FilialForm(request.POST)
        if filial_form.is_valid():
            data = filial_form.cleaned_data
            filial.nombre = data["name"]
            filial.sede = data["n_sede"]
            filial.save()
            return render(request, 'core/index.html')
    else:
        # Mediante método GET
        filial_form = FilialForm(initial={'name': filial.nombre, 'n_sede': filial.sede})
        
        return render(request, 'core/editar_filial.html', {'form': filial_form})

def eliminar(request , id_filial):

    filial = Filial.objects.get(id=id_filial)
    name = filial.nombre
    filial.delete()

    return render(request, 'core/eliminar_filial.html', {"nombre_eliminado": name})

def acerca_de_mi(request):
    return render (request, 'core/about.html')

#basada en clases


