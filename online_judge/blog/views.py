from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	context = {}
	return render(request, 'blog/home.html', context)

def about(request):
	context = {}
	return render(request, 'blog/about.html', context)


