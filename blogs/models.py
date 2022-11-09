from django.db import models

# Create your models here.
class MyBlog(models.Model):
	judul = models.CharField(verbose_name="Judul Artikel",max_length=200,null=False,blank=False,default="-")
	creator = models.CharField(verbose_name="Pembuat",max_length=200,null=False,blank=False,default="-")
	paragrafs = models.TextField(verbose_name="Artikel",max_length=5000)
	tanggalbuat = models.DateTimeField(verbose_name="Tanggal Pembuatan",auto_now=True)
	foto = models.ImageField(upload_to='img',default="",verbose_name="Gambar untuk Artikel")

	def __str__(self):
		return "%s - %s"%(self.judul,self.creator)

	class Meta:
		ordering = ['tanggalbuat','judul','paragrafs']
		unique_together = ['judul','creator','paragrafs']
