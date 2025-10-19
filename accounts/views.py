from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def redirect_if_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

@redirect_if_authenticated
def login_page(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() # <-- This gets the authenticated user
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home")
    else:
        form = CustomAuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})

@redirect_if_authenticated
def register_page(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 1. Save the form and get the new user object.
            user = form.save()
            # 2. Log the new user in.
            user.backend = 'accounts.backends.EmailBackend'
            login(request, user)
            
            # 3. Create a more welcoming success message.
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")
            
            # 4. Redirect to the home page, not the login page.
            return redirect("home")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


def logout_page(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')