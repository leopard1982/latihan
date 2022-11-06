from django.shortcuts import render, HttpResponse
from .forms import InputDaftarNama
from .models import DaftarNama

from django.views import View

# Create your views here.
class IndexViewClass(View):
    template_name = "indeks.html"
    context = {
        'heading': 'Menambahkan Daftar Nama'
    }
    def get(self,request):
        return render(request,self.template_name,self.context)



def indeks2(request):
    if request.method == 'POST':
        forms = InputDaftarNama(request.POST)
        if forms.is_valid():
            forms.save()

    forms = InputDaftarNama()
    data = DaftarNama.objects.all()[2:3]
    return render(request,'indeks.html',{'forms':forms,'data':data})