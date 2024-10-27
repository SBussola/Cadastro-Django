from django.db import models

class Usuario (models.Model):
    id_usuario = models.AutoField (primary_key=True)
    nome = models.CharField (max_length=255)
    idade = models.IntegerField()
    
    def __str__(self):
        return self.nome  # Isso ajuda a identificar o 
    #objeto no admin e nas consultas