from django import forms
from .models import bakso

class FormAddBakso(forms.ModelForm):
    class Meta:
        model = bakso
        fields = {
            'nama',
            'gambar',
            'harga',
            'kategori'
        }
        widgets = {
            'nama': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Bakso'}),
            'gambar': forms.FileInput(attrs={'class':'form-control', 'type':'file'}),
            'harga': forms.NumberInput(attrs={'class':'form-control','placeholder':'Harga Bakso'}),
            'kategori': forms.Select(attrs={'class':'custom-select'})
        }