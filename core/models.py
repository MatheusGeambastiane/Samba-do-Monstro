from tabnanny import verbose
from django.db import models
from django.core.validators import validate_email

# Create your models here.
class Convidados(models.Model):
    CHOICES = (
        ('30','R$ 30,00 - Vou só comer'),
        ('50','R$ 50,00 - Vou encher a cara e comer')
    )

    nome = models.CharField(max_length=100, verbose_name="Nome da Lenda", help_text="Escreva seu nome, escreva sua história",
                             null=False)
    email = models.EmailField(validators=[validate_email], verbose_name="seu email")
    telefone = models.CharField(max_length=20, verbose_name="Telefone", null=True)
    opcao = models.CharField(max_length=50, verbose_name="opções", choices=CHOICES)
    pagou = models.BooleanField(verbose_name="Pagou?", help_text="Pagou o filha da puta ou deu uma de Yan?", default=False)

    def __str__(self) -> str:
        return self.nome

    class Meta: 
        verbose_name = 'Convidado'
        verbose_name_plural = 'Convidados'
        