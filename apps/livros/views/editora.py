from django.shortcuts import render, redirect, get_object_or_404
from apps.livros.models import Editora
from django.contrib import messages

def cria_editora(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        if not nome.strip():
            print('O campo nome não pode ficar em branco!')
            return redirect('cria_editora')
        cidade = request.POST['cidade']
        if not cidade.strip():
            print('O campo cidade não pode ficar em branco!')
            return redirect('cria_editora')
        estado = request.POST['estado']
        if not estado.strip():
            print('O campo estado não pode ficar em branco!')
            return redirect('cria_editora')
        editora = Editora.objects.create(nome=nome, cidade=cidade, estado=estado)
        editora.save()
        return redirect('lista_editoras')
    else:
        return render(request, 'editoras/cria_editora.html')

def lista_editoras(request):
    editoras = Editora.objects.all()
    dados = {
        'editoras': editoras
    }
    return render(request, 'editoras/lista.html', dados)

def deleta_editora(request, editora_id):
    editora = get_object_or_404(Editora, pk=editora_id)
    try:
        editora.delete()
    except OSError:
        messages.error(request, 'Editora não pode ser deletada!')
    else:
        messages.success(request, 'Editora deletada com sucesso!')

    return redirect('lista_editoras')

def edita_editora(request, editora_id):
    editora = get_object_or_404(Editora, pk=editora_id)

    dados = {
        'editora': editora
    }

    return render(request, 'editoras/edita_editora.html', dados)

def atualiza_editora(request):
    if request.method == 'POST':
        editora_id = request.POST['editora_id']
        e = get_object_or_404(Editora, pk=editora_id)
        e.nome = request.POST['nome']
        e.cidade = request.POST['cidade']
        e.estado = request.POST['estado']
        e.save()
        messages.success(request, 'Editora atualizada com sucesso!')
        return redirect('lista_editoras')