from django.contrib import admin
from .models import Convidados

@admin.register(Convidados)
class ConvidadosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'opcao', 'pagou')
    fields = ('nome', 'opcao', 'email', 'telefone', 'pagou')
    search_fields = ('nome',)
    list_filter = ('opcao',)
# Register your models here.
