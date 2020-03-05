from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


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
    return render(request, 'users/profile.html')
