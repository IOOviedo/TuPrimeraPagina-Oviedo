from django import forms


class PeliculaFormulario(forms.Form):
    titulo = forms.CharField(max_length=50)
    director = forms.CharField(max_length=50)

class ElencoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)

class MusicaFormulario(forms.Form):
    cancion = forms.CharField(max_length=50)
    interprete = forms.CharField(max_length=50)

