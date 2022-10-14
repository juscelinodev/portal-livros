from asyncio.base_subprocess import BaseSubprocessTransport
import email
# from pyexpat.errors import messages
from django.contrib import messages
from re import sub
from django.shortcuts import render, redirect
from portal.models import Autor, Livro
from portal.forms import AutorForm, LivroForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login')
def autor(request):
    autores = Autor.objects.all()

    context = {
        'autores' : autores
    }
    return render(request, 'autor.html', context)

@login_required(login_url='/login')
def livro(request):
    livros = Livro.objects.all()

    context = {
        'livros' : livros
    }
    return render(request, 'livro.html', context)

def autor_add(request):
    if request.method == 'GET':
        return render (request, 'autor_add.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')

        autor = Autor.objects.filter(email=email).first()
        if autor:
            messages.info(request, 'Esse email de usuário já está cadastrado em nosso sistema!')
            return redirect('autor_add')
        else:
            autor = Autor(nome = nome, email = email, data_nascimento = data_nascimento)
            autor.save()
            messages.info(request, 'Autor cadastrado com sucesso!')
            return redirect('autor')


def autor_edit(request,autor_pk):
    autor = Autor.objects.get(pk=autor_pk)

    form = AutorForm(request.POST or None, instance=autor)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect ('autor')

    context = {
        'autor': autor.id,
        'form': form,
    }

    return render(request, 'autor_edit.html', context)


def autor_delete(request,autor_pk):
    autor = Autor.objects.get(pk=autor_pk)
    autor.delete()
    return redirect ('autor')


def livro_add(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        context = {
            'autores':autores
        }
        return render (request, 'livro_add.html',context)
    else:
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        data_lancamento = request.POST.get('data_lancamento')
        isbn = request.POST.get('isbn')
        numero_paginas = request.POST.get('numero_paginas')
        autor = request.POST.get('autor')
        autor = Autor.objects.get(id=autor)

        buscatitulo = Livro.objects.filter(titulo=titulo).first()
        if buscatitulo:
            messages.info(request, 'Esse titulo já está cadastrado em nosso sistema')
            return redirect('livro_add')
        else:
            buscaisbn = Livro.objects.filter(isbn=isbn).first()
            if buscaisbn:
                messages.info(request, 'Já existe uma ISBN com essa numeração cadastrada em nosso sistema')
                return redirect('livro_add')
            else:
                livro = Livro(titulo=titulo, subtitulo=subtitulo, autor=autor, data_lancamento=data_lancamento, isbn=isbn, numero_paginas=numero_paginas)
                livro.save()
                messages.info(request, 'Livro cadastrado com sucesso!')
                return redirect('livro')


def livro_edit(request,livro_pk):
    livro = Livro.objects.get(pk=livro_pk)

    form = LivroForm(request.POST or None, instance=livro)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect ('livro')

    context = {
        'livro': livro.id,
        'form': form,
    }

    return render(request, 'livro_edit.html', context)


def livro_delete(request,livro_pk):
    livro = Livro.objects.get(pk=livro_pk)
    livro.delete()
    return redirect ('livro')



def cadastro(request):
    if request.method == 'GET':
        return render (request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        count_nums = 0
        # checagem de caracteres
        for c in nome:
            if c.isdigit():
                count_nums += 1
        if count_nums > 0:
            messages.info(request, 'O nome deve conter apenas letras')
            return redirect('cadastro')
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(username.strip()) == 0:
            messages.info(request, 'Favor inserir corretamente nos campos nome, email e usuário.')
            return redirect('cadastro')
        if len(senha) < 6 or len(senha) > 10:
            messages.info(request, 'Favor inserir senha com no mínimo 6 e no máximo 10 caracteres')
            return redirect('cadastro')
    # contadores
    count_alpha = 0
    count_nums = 0
    # checagem de caracteres
    for c in senha:
        if c.isalpha():
            count_alpha += 1
        elif c.isdigit():
            count_nums += 1
    if count_alpha == 0 or count_nums == 0:
        messages.info(request, 'A senha deve conter letras e números')
        return redirect('cadastro')
    user = User.objects.filter(email=email).first()
    if user:
        messages.info(request, 'Esse email de usuário já está cadastrado em nosso sistemas!')
        return redirect('cadastro')
    else:
        user = User.objects.filter(username=username).first()
        if user:
            messages.info(request, 'Já existe um usuário com esse username!')
            return redirect('cadastro') 
        else:
            user = User.objects.create_user(first_name = nome, last_name = sobrenome, email = email, username = username, password = senha)
            user.save()
            messages.info(request, 'Usuário cadastrado com sucesso!')
            return redirect('home')
                

def login(request):
    if request.method == 'GET':
        return render (request, 'login.html')
    else:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return render(request, 'home.html')
        else:
            messages.info(request, 'Usuário ou senha inválidos!')
            return redirect('login')
        

def logout(request):
    logout_django(request)
    return render(request, 'home.html')
    
 