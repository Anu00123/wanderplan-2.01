from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import logout

def auth_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'signup':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('signup-email')
            password = request.POST.get('signup-password')
            confirm_password = request.POST.get('confirm-password')

            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                CustomUser.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                messages.success(request, "Signup successful. Please login.")

        elif action == 'login':
            email = request.POST.get('login-email')
            password = request.POST.get('login-password')

            user = CustomUser.objects.filter(email=email, password=password).first()
            if user:
                request.session['user_id'] = user.id
                messages.success(request, "Login successful.")
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials.")

    return render(request, 'auth.html')



def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('auth_page')  