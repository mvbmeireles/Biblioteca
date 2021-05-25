from django.contrib import admin
from .models import Autor, Genero, Livro, Informações

# Register your models here.

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Informações)