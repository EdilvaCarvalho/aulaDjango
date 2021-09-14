from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from apps.livros.models import Livro
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco!')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco!')
            return redirect('cadastro')
        if not senha1.strip():
            print('O campo senha não pode ficar em branco!')
            return redirect('cadastro')
        if not senhas_iguais(senha1, senha2):
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')
        usuario = User.objects.create_user(username=nome, email=email, password=senha1)
        usuario.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if senha.strip() == "":
            messages.error(request, 'O campo senha não pode ficar em branco!')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            usuario = auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('dashboard')
            else:
                messages.error(request, 'O email ou senha estão incorretos!')
        else:
            messages.error(request, 'O email ou senha estão incorretos!')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        livros = Livro.objects.filter(usuario=id)
        dados = {
            'livros': livros
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def edita_usuario(request):
    return render(request, 'usuarios/edita_usuario.html')

def atualiza_usuario(request):
    if request.method == 'POST':
        u = get_object_or_404(User, pk=request.user.id)
        u.username = request.POST['nome']
        u.email = request.POST['email']
        if senhas_iguais(request.POST['senha1'], request.POST['senha2']):
            u.set_password(request.POST['senha1'])
        else:
            messages.error(request, 'As senhas não são iguais!')
            return redirect('atualiza_usuario')
        u.save()
        messages.success(request, 'Usuario atualizado com sucesso!')
        return redirect('dashboard')

def senhas_iguais(senha1, senha2):
    return senha1 == senha2