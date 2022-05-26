from django.shortcuts import render
from django.views.generic.edit import CreateView
#MyApps
from .models import Convidados

class ConvidadosView(CreateView):
    model = Convidados
    fields = '__all__'
    template_name = 'frontend/index.html'
    success_url = 'frontend/inner-page.html'
