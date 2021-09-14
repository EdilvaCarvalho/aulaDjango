from django.contrib import admin
from .models import Editora, Autor, Livro

class ListandoEditoras(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 5

class ListandoAutores(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 5

class ListandoLivros(admin.ModelAdmin):
    list_display = ('id', 'nome', 'genero', 'publicado')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('genero', 'autor', 'editora')
    list_editable = ('publicado',)
    list_per_page = 5

admin.site.register(Editora, ListandoEditoras)
admin.site.register(Autor, ListandoAutores)
admin.site.register(Livro, ListandoLivros)

# Register your models here.
