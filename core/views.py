from urllib import request
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView

#MyApps
from .models import Convidados

class ConvidadosView(CreateView):
    model = Convidados
    fields = '__all__'
    template_name = 'frontend/index.html'
    success_url = '/sucess/'

class Sucessview(CreateView):
    model = Convidados
    fields = '__all__'
    template_name = 'frontend/inner-page.html'
