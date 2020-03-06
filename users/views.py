from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.

def register(request):
    # If Http request is using Post method
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # Extract information
        if form.is_valid():
            form.save()  # save user and hashed password
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to login {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    # pass the template and pass form as dictionary
    return render(request, 'users/register.html', {'form': form})


@login_required         # change this function to login required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # If they are valid save...
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Dictionary to access within the HTML
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)
