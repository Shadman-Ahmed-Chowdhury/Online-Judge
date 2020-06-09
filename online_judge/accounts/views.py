from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerPage(request): 
	if request.user.is_authenticated:
		return redirect('accounts:index')
	else: 
		form = CreateUserForm()

		if request.method == 'POST': 
			form = CreateUserForm(request.POST)
			if form.is_valid(): 
				form.save() 
				user = form.cleaned_data.get('username')
				messages.success(request, 'Sign Up successful for ' + user)
				return redirect('accounts:login')


		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request): 
	if request.user.is_authenticated:
		return redirect('accounts:index')
	else: 
		if request.method == 'POST': 
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None: 
				login(request, user)
				return redirect('accounts:index')
			else: 
				messages.info(request, 'Username or Password is incorrect!')
		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request): 
	logout(request)
	return redirect('accounts:login')

def index(request): 
	return render(request, 'accounts/index.html')
