from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import *
from . import forms
from .models import *

# Create your views here.
class BaksoView(ListView):
    queryset = bakso.objects.all()
    template_name = 'bakso/index.html'
    
# class CreateView(CreateView):
#     model = bakso
#     form_class = forms.FormBakso
#     template_name = 'bakso/add-bakso.html'
#     success_url = reverse_lazy('bakso:index')
    