from django.shortcuts import render, redirect

# Create your views here.

from .models import Pelicula, Elenco, Musica
from .forms import PeliculaFormulario, ElencoFormulario, MusicaFormulario

def inicio(request):

    print(f"metodo: {request.method}")

    return render(request, 'inicio.html')

def peliculas(request):

    peliculas = Pelicula.objects.all()

    contexto = {"peliculas" : peliculas,}
    return render(request, 'peliculas.html', contexto)

def elenco(request):

    elenco = Elenco.objects.all()

    contexto = {"elenco" : elenco,}
    return render(request, 'elenco.html', contexto)

def musica(request):

    musica = Musica.objects.all()

    contexto = {"musica" : musica,}
    return render(request, 'musica.html', contexto)

def pelicula_formulario(request):
    if request.method == 'POST':
        form = PeliculaFormulario(request.POST)
        if form.is_valid():
            print("El formulario es valido")
            pelicula = Pelicula(titulo=form.cleaned_data['titulo'], director=form.cleaned_data['director'])
            pelicula.save()
            return redirect('inicio')

    form = PeliculaFormulario()
    return render(request, 'pelicula_formulario.html',{'form': form})

def elenco_formulario(request):
    if request.method == 'POST':
        form = ElencoFormulario(request.POST)
        if form.is_valid():
            print("El formulario es valido")
            elenco = Elenco(nombre=form.cleaned_data['nombre'], apellido=form.cleaned_data['apellido'])
            elenco.save()
            return redirect('inicio')

    form = ElencoFormulario()
    return render(request, 'elenco_formulario.html',{'form': form})

def musica_formulario(request):
    if request.method == 'POST':
        form = MusicaFormulario(request.POST)
        if form.is_valid():
            print("El formulario es valido")
            musica = Musica(cancion=form.cleaned_data['cancion'], interprete=form.cleaned_data['interprete'])
            musica.save()
            return redirect('inicio')

    form = MusicaFormulario()
    return render(request, 'musica_formulario.html',{'form': form})
