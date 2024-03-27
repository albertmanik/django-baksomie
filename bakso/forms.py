from django import forms
from .models import bakso

class FormBakso(forms.ModelForm):
    class Meta:
        model = bakso
        fields = (
            'nama',
            'gambar',
            'harga',
            'kategori',
            'deskripsi'
        )
        widgets = {
            'nama': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Bakso'}),
            'gambar': forms.FileInput(attrs={'class':'form-control', 'type':'file'}),
            'harga': forms.NumberInput(attrs={'class':'form-control','placeholder':'Harga Bakso', 'type':'number'}),
            'kategori': forms.Select(attrs={'class':'form-control digits'}),
            'deskripsi': forms.Textarea(attrs={'id':'editor1','cols':'10','rows':'4','placeholder':'Masukkan Deskripsi'})
        }