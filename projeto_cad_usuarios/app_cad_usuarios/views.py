from django.shortcuts import render
from .models import Usuario

def home (request):
    return render(request, 'usuarios/home.html')

def usuarios (request):
    #salvar os dados da tela para o banco de dados, criado no models.py
    #podendo ser vizualisado na extensão SQLite Viewer
    novo_usuario = Usuario()
    novo_usuario.nome= request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    #exibir todos os usuarios já cadastrado em uma nova página
    #vamos buscar os dados, mas antes de colocar vamos add em um dicionário
    # que é o formato que o Django espera
    
    usuarios={
        'usuarios': Usuario.objects.all()
    }
    #Agora retornamos os dados na página de listagem de usuarios
    return render (request, 'usuarios/usuarios.html',usuarios)