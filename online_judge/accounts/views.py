from django.shortcuts import render, redirect
from .forms import CreateUserForm

# Create your views here.

def registerPage(request): 
	form = CreateUserForm()

	if request.method == 'POST': 
		form = CreateUserForm(request.POST)
		if form.is_valid(): 
			form.save() 
			return redirect('accounts:login')


	context = {'form':form}
	return render(request, 'accounts/register.html', context)

def loginPage(request): 
	context = {}
	return render(request, 'accounts/login.html')

def index(request): 
	return render(request, 'accounts/index.html')
