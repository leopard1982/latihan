from django.shortcuts import render, HttpResponse

from django.http import HttpResponseRedirect

from .forms import InputMyBlog
from .models import MyBlog

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.core.paginator import Paginator

# Create your views here.
def indeks(request):
	data =MyBlog.objects.all()
	p = Paginator(data,2)
	page = request.GET.get('page')
	blogs = p.get_page(page)

	'''give the lastsest post'''
	lastdata = MyBlog.objects.all().order_by('-id')[:1]
	return render(request,'blogs/indeks.html',{'blogs':blogs,'lastdata':lastdata})

def read_article(request,yangmana):
	blogs = MyBlog.objects.get(judul=yangmana)
	'''give the lastsest post'''
	lastdata = MyBlog.objects.all().order_by('-id')[:1]
	return render(request,'blogs/view-detail.html',{'blogs':blogs,'lastdata':lastdata})


def Insert_InputMyBlog(request):
	if request.method=="POST":
		forms = InputMyBlog(request.POST,request.FILES)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/blogs/')
		else:
			print(forms)

	forms = InputMyBlog(initial={'creator':request.user.username})
	'''give the lastsest post'''
	lastdata = MyBlog.objects.all().order_by('-id')[:1]
	return render(request,'blogs/input-blogs.html',{'forms':forms,'lastdata':lastdata})

def Delete_InputMyBlog(request,judul):
	myblogs = MyBlog.objects.filter(judul=judul)
	if myblogs.exists():
		MyBlog.objects.filter(judul=judul).delete()
	return HttpResponseRedirect('/blogs/')

def LoginUser(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']

		usernya = authenticate(username=username,password=password)
		if(usernya is not None):
			login(request,usernya)
			
	return HttpResponseRedirect('/blogs/')

def LogoutUser(request):
	logout(request)
	return HttpResponseRedirect('/blogs/')