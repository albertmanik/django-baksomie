from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from . import forms
from .forms import *

# Create your views here.
class BaksoView(ListView):
    queryset = bakso.objects.all()
    template_name = 'index.html'
    
class CreateView(CreateView):
    model = bakso
    form_class = forms.FormAddBakso
    template_name = 'bakso\bakso-add.html'
    success_url = reverse_lazy('bakso:index')
    