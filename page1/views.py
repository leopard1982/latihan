from django.shortcuts import render, HttpResponse
from .forms import InputDaftarNama
from .models import DaftarNama

from django.views import generic

# Create your views here.
def indeks(request):
    if request.method == 'POST':
        forms = InputDaftarNama(request.POST)
        if forms.is_valid():
            forms.save()

    forms = InputDaftarNama()
    data = DaftarNama.objects.all()[2:3]
    return render(request,'indeks.html',{'forms':forms,'data':data})

def indeks2(request):
    if request.method == 'POST':
        forms = InputDaftarNama(request.POST)
        if forms.is_valid():
            forms.save()

    forms = InputDaftarNama()
    data = DaftarNama.objects.all()[2:3]
    return render(request,'indeks.html',{'forms':forms,'data':data})