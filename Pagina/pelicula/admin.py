from django.contrib import admin

# Register your models here.
from .models import Pelicula, Elenco, Musica

admin.site.register(Pelicula)
admin.site.register(Elenco)
admin.site.register(Musica)