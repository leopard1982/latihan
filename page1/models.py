from django.db import models

# Create your models here.
class DaftarNama(models.Model):
    nama = models.CharField(max_length=100, verbose_name="Nama Anda",null=False,blank=False)
    alamat = models.CharField(max_length=100, verbose_name="Alamat Anda",null=False, blank=False)

    def __str__(self):
        return "%s - %s" % (self.nama, self.alamat)
    
    class Meta:
        ordering = ['nama']
        unique_together = ['nama','alamat']