from django.db import models

# Create your models here.
class bakso(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=20)
    gambar = models.FileField(upload_to='bakso/')
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    KATEGORI_CHOICES = (
        ('bakso', 'Bakso'),
        ('ayam', 'Ayam'),
    )
    kategori = models.CharField(max_length=5, choices=KATEGORI_CHOICES)
    
    def __str__(self):
        return self.nama