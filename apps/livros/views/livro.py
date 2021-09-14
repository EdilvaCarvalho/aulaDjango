from django.shortcuts import render, get_object_or_404, redirect
from apps.livros.models import Livro, Autor, Editora
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

def index(request):

    livros = Livro.objects.filter(publicado=True)
    paginator = Paginator(livros, 6)
    page = request.GET.get('page')
    livros_por_pagina = paginator.get_page(page)
    dados = {
        'livros': livros_por_pagina
    }
    return render(request, 'index.html', dados)

def livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    livro_a_exibir = {
        'livro': livro
    }
    return render(request, 'livro.html', livro_a_exibir)

def buscar(request):
    lista_livros = Livro.objects.filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_livros = lista_livros.filter(nome__icontains=nome_a_buscar)

    dados = {
        'livros': lista_livros
    }

    return render(request, 'buscar.html', dados)

def cria_livro(request):
    autores = Autor.objects.all()
    editoras = Editora.objects.all()

    dados = {
        'autores': autores,
        'editoras': editoras
    }

    if request.method == 'POST':
        usuario = get_object_or_404(User, pk=request.user.id)
        nome = request.POST['nome']
        genero = request.POST['genero']
        qtd_paginas = request.POST['qtd_paginas']
        ano_pub = request.POST['ano_pub']
        resenha = request.POST['resenha']
        autores_id = request.POST.getlist('autor')
        lista_autores = []
        for id in autores_id:
            autor = get_object_or_404(Autor, pk=id)
            lista_autores.append(autor)
        editora_id = request.POST['editora']
        editora = get_object_or_404(Editora, pk=editora_id)
        capa_livro = request.FILES['capa_livro']
        livro = Livro.objects.create(usuario=usuario, nome=nome, genero=genero, qtd_paginas=qtd_paginas, ano_pub=ano_pub,
                                     resenha=resenha, editora=editora, capa_livro=capa_livro)
        livro.autor.set(lista_autores)
        livro.save()
        messages.success(request, 'Livro cadastrado com sucesso!')
        return redirect('dashboard')
    else:
        return render(request, 'livros/cria_livro.html', dados)

def deleta_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    livro.delete()
    messages.success(request, 'Livro deletado com sucesso!')
    return redirect('dashboard')

def edita_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    autores = Autor.objects.all()
    editoras = Editora.objects.all()

    dados = {
        'autores': autores,
        'editoras': editoras,
        'livro': livro
    }

    return render(request, 'livros/edita_livro.html', dados)

def atualiza_livro(request):
    if request.method == 'POST':
        livro_id = request.POST['livro_id']
        l = get_object_or_404(Livro, pk=livro_id)
        l.nome = request.POST['nome']
        l.genero = request.POST['genero']
        l.qtd_paginas = request.POST['qtd_paginas']
        l.ano_pub = request.POST['ano_pub']
        l.resenha = request.POST['resenha']
        autores_id = request.POST.getlist('autor')
        lista_autores = []
        for id in autores_id:
            autor = get_object_or_404(Autor, pk=id)
            lista_autores.append(autor)
        editora_id = request.POST['editora']
        l.editora = get_object_or_404(Editora, pk=editora_id)
        l.autor.set(lista_autores)
        if 'capa_livro' in request.FILES:
            l.capa_livro = request.FILES['capa_livro']
        l.save()
        messages.success(request, 'Livro atualizado com sucesso!')
        return redirect('dashboard')
