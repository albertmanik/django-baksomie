from django.views.generic import ListView
from django.views import View
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import *
from . import forms
from .models import *
import os

# Create your views here.
class BaksoView(ListView):
    queryset = bakso.objects.all()
    template_name = 'bakso/index.html'
    
class CreateView(CreateView):
    model = bakso
    form_class = forms.FormBakso
    template_name = 'bakso/bakso-add.html'
    success_url = reverse_lazy('bakso:list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Mengatur instance ke objek baru untuk membuat formulir kosong
        kwargs['instance'] = bakso()
        return kwargs
    
class UpdateView(UpdateView):
    model = bakso
    form_class = forms.FormBakso
    template_name = 'bakso/bakso-edit.html'
    # def get_success_url(self):
    #     return reverse_lazy('bakso:list')
    success_url = reverse_lazy('bakso:list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()  # Setel instance dengan objek yang ingin Anda edit
        return kwargs
    
class DeleteBaksoView(View):
     def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        # Dapatkan objek bakso yang akan dihapus
        bakso_obj = bakso.objects.get(pk=pk)
        
        # Dapatkan path dari file gambar yang terkait dengan objek bakso
        file_path = bakso_obj.gambar.path
        
        # Hapus file gambar dari sistem file jika ada
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Hapus objek bakso dari database
        bakso_obj.delete()
        return redirect('/dashboard/bakso/list/')