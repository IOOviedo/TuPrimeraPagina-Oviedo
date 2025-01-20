from django.urls import path

from .views import peliculas, inicio, elenco, musica, PeliculaFormulario, ElencoFormulario, MusicaFormulario

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('pelicula/', peliculas, name="peliculas"),
    path('elenco/', elenco, name="elenco"),
    path('musica/', musica, name="musica"),
    path("pelicula-nueva", PeliculaFormulario, name="pelicula_formulario"),
    path("actor-nuevo", ElencoFormulario, name="elenco_formulario"),
    path("musica-nueva", MusicaFormulario, name="musica_formulario"),
]