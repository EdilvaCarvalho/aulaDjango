from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:livro_id>', livro, name='livro'),
    path('buscar', buscar, name='buscar'),
    path('cria/livro', cria_livro, name='cria_livro'),
    path('deleta/<int:livro_id>', deleta_livro, name='deleta_livro'),
    path('edita/<int:livro_id>', edita_livro, name='edita_livro'),
    path('atualiza_livro', atualiza_livro, name='atualiza_livro'),
    path('cria/autor', cria_autor, name='cria_autor'),
    path('deleta_autor/<int:autor_id>', deleta_autor, name='deleta_autor'),
    path('edita_autor/<int:autor_id>', edita_autor, name='edita_autor'),
    path('atualiza_autor', atualiza_autor, name='atualiza_autor'),
    path('lista_autores', lista_autores, name='lista_autores'),
    path('cria/editora', cria_editora, name='cria_editora'),
    path('deleta_editora/<int:editora_id>', deleta_editora, name='deleta_editora'),
    path('edita_editora/<int:editora_id>', edita_editora, name='edita_editora'),
    path('atualiza_editora', atualiza_editora, name='atualiza_editora'),
    path('lista_editoras', lista_editoras, name='lista_editoras'),
]