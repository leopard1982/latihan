from django.shortcuts import render, HttpResponse
from .forms import InputDaftarNama
from .models import DaftarNama

from django.views import View

from django.views.generic.list import ListView


# Create your views here.
class Parameterku(View):
    def post(self,request,parameter):
        return HttpResponse("Dari POST, parameternya itu ya: " + parameter)

    def get(self,request,parameter):
        return HttpResponse("Dari GET, parameternya adalah: " + parameter)

class IndexViewClass(View):
    hasil=False
    def post(self,request):
        forms = InputDaftarNama(request.POST)
        if forms.is_valid():
            forms.save()
        forms = InputDaftarNama(initial={'nama':request.POST['nama'],'alamat':request.POST['alamat']})
        data = DaftarNama.objects.all()
        return render(request,'indeks.html',{'forms':forms,'data':data,'hasil':self.hasil})
    
    def get(self,request):
        forms = InputDaftarNama(initial={
            'nama':'xxxxxx',
            'alamat':'yyyyyy'
            })
        data = DaftarNama.objects.all()
        return render(request,'indeks.html',{'forms':forms,'data':data,'hasil':self.hasil}) 

def indeks2(request):
    if request.method == 'POST':
        forms = InputDaftarNama(request.POST)
        if forms.is_valid():
            forms.save()

    forms = InputDaftarNama()
    data = DaftarNama.objects.all()[2:3]
    return render(request,'indeks.html',{'forms':forms,'data':data})