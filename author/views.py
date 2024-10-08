from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, editUserForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        register_form = RegisterForm()

    return render(request, 'register.html', {'form': register_form, 'type': 'Register'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            user_pass = form.cleaned_data.get('password')

            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('homepage')
            else:
                messages.warning(request, 'Login information incorrect')
    else:
        form = AuthenticationForm()

    return render(request, 'register.html', {'form': form, 'type': 'Login'})

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('homepage')

def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


def edit_profile(request):
    if request.method == 'POST':
        form = editUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        form = editUserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html', {'form': form})

def change_pass1(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    
    return render(request, 'change_pass1.html', {'form': form})