from django.shortcuts import render, HttpResponse

from .models import DaftarNama

from .forms import InputDaftarNama

#coba paginator
from django.core.paginator import Paginator

# Create your views here.
def indeks(request):
	if request.method=="POST":
		forms = InputDaftarNama(request.POST)
		if forms.is_valid():
			forms.save()

	forms = InputDaftarNama()

	p=Paginator(DaftarNama.objects.all(),2)
	page = request.GET.get('page')
	halaman = p.get_page(page)
	return render(request,'paging/indeks.html',{'forms':forms,'halaman':halaman})