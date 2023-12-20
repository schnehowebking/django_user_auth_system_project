from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import *
# Create your views here.
def home(request):
    return render(request, './loginlogout/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully. You are now logged in.')
            return redirect('profile')
    else:
        form = UserSignUpForm()

    return render(request, './loginlogout/signup.html', {'form': form})
    


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, './loginlogout/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, './loginlogout/profile.html')
    

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Password changed successfully.')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, './loginlogout/change_password.html', {'form': form})

@login_required
def change_password_without(request):
    if request.method == 'POST':
        form = UserChangePasswordwithoutForm(request.POST)
        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Password changed successfully.')
            return redirect('profile')
    else:
        form = UserChangePasswordwithoutForm()

    return render(request, './loginlogout/change_password.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('home')