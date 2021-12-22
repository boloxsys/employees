from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
#import models
from .models import Prueba
#vistas genericas - ejemplo con TemplateView
from .forms import PruebaForm

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['1', '9', '22', '390', '98']

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'
    

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '/'
