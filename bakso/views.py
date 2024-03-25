from django.views.generic import ListView
from django.views import View
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import *
from . import forms
from .models import *

# Create your views here.
class BaksoView(ListView):
    queryset = bakso.objects.all()
    template_name = 'bakso/index.html'
    
class CreateView(CreateView):
    model = bakso
    form_class = forms.FormBakso
    template_name = 'bakso/bakso-add.html'
    success_url = reverse_lazy('bakso:list')
    
    
class DeleteBaksoView(View):
     def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        bakso.objects.filter(pk=pk).delete()
        return redirect('/dashboard/bakso/')