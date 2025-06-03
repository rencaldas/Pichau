from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # adicione logout aqui
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=senha)
            if user:
                login(request, user)
                return redirect('/')
            else:
                erro = "Credenciais inválidas"
                return render(request, 'contas/login.html', {'erro': erro})
        except User.DoesNotExist:
            return render(request, 'contas/login.html', {'erro': 'Email não encontrado'})
    return render(request, 'contas/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        confirmacao = request.POST['confirmar_senha']
        if senha != confirmacao:
            return render(request, 'contas/cadastro.html', {'erro': 'Senhas não coincidem'})
        if User.objects.filter(email=email).exists():
            return render(request, 'contas/cadastro.html', {'erro': 'Email já cadastrado'})
        usuario = User.objects.create_user(username=email, email=email, password=senha)
        login(request, usuario)
        return redirect('/')
    return render(request, 'contas/cadastro.html')

def logout_view(request):
    logout(request)
    return redirect('/')
