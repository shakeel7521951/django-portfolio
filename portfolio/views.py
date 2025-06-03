from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser, Project, Skill, Service,Contact

def home(request):
    profile = CustomUser.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html', {'profile': profile, 'projects': projects, 'skills': skills})

def about(request):
    profile = CustomUser.objects.first()
    return render(request, 'about.html', {'profile': profile})

def service(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, "Thank you for contacting us! We'll get back to you soon.")
        return redirect('contact')

    return render(request, 'contact.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully. You can now log in.')
        return redirect('login')

    return render(request, 'signup.html')

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')
