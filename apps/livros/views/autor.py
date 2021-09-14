from django.shortcuts import render, redirect, get_object_or_404
from apps.livros.models import Autor
from django.contrib import messages

def cria_autor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        if not nome.strip():
            print('O campo nome não pode ficar em branco!')
            return redirect('cria_autor')
        data_nasc = request.POST['data_nasc']
        if not data_nasc.strip():
            print('O campo data de nascimento não pode ficar em branco!')
            return redirect('cria_autor')
        nacionalidade = request.POST['nacionalidade']
        if not nacionalidade.strip():
            print('O campo nacionalidade não pode ficar em branco!')
            return redirect('cria_autor')
        sexo = request.POST['sexo']
        autor = Autor.objects.create(nome=nome, data_nasc=data_nasc, nacionalidade=nacionalidade, sexo=sexo)
        autor.save()
        return redirect('lista_autores')
    else:
        return render(request, 'autores/cria_autor.html')

def lista_autores(request):
    autores = Autor.objects.all()
    dados = {
        'autores': autores
    }
    return render(request, 'autores/lista.html', dados)

def deleta_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    try:
        autor.delete()
    except OSError:
        messages.error(request, 'Autor não pode ser deletado!')
    else:
        messages.success(request, 'Autor deletado com sucesso!')
    return redirect('lista_autores')

def edita_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)

    dados = {
        'autor': autor
    }

    return render(request, 'autores/edita_autor.html', dados)

def atualiza_autor(request):
    if request.method == 'POST':
        autor_id = request.POST['autor_id']
        a = get_object_or_404(Autor, pk=autor_id)
        a.nome = request.POST['nome']
        a.data_nasc = request.POST['data_nasc']
        a.nacionalidade = request.POST['nacionalidade']
        a.sexo = request.POST['sexo']
        a.save()
        messages.success(request, 'Autor atualizado com sucesso!')
        return redirect('lista_autores')