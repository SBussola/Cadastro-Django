from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view, responsavel, nome da referencia
    #usuarios.com
    path ('',views.home, name ='home'),
    #usuarios.com/usuarios
    path ('usuarios/', views.usuarios, name= 'listagem_usuarios')
]
