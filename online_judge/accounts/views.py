from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, CreateProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

def registerPage(request): 
	if request.user.is_authenticated:
		return redirect('accounts:index')
	else: 
		form = CreateUserForm()

		if request.method == 'POST': 
			form = CreateUserForm(request.POST)
			if form.is_valid(): 
				user = form.save() 
				username = form.cleaned_data.get('username')
				messages.success(request, 'Sign Up successful for ' + username)
				Profile.objects.create(user=user)
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


@login_required
def profile(request):
	return render(request, 'accounts/profile.html')

@login_required	
def profile_update(request): 
	if request.method == 'POST': 
		user_update_form = UserUpdateForm(request.POST, instance=request.user) 
		profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) 
		
		if user_update_form.is_valid() and profile_update_form.is_valid(): 
			user_update_form.save() 
			profile_update_form.save()
			messages.success(request, 'Your profile has been updated')
			return redirect('accounts:profile')
	else: 
		user_update_form = UserUpdateForm(instance=request.user)
		profile_update_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'user_update_form': user_update_form, 
		'profile_update_form': profile_update_form
	}
	return render(request, 'accounts/profile_update.html', context)



def index(request): 
	return render(request, 'accounts/index.html')
