from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm

# Views for login and logout

# Register a user or return the register page
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for \'{username}\'. Please log in now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Log a user in or return the login page
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.get_user()
            login(request, username)
            messages.success(request, f'Successfully logged in as \'{username}\'')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
    else:
        form = AuthenticationForm
    return render(request, 'users/login.html', {'form': form})

# Log a user out and redirect to login
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, f'Successfully logged out')
        return redirect('login')
