from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.

def index(request):
    book = Product.objects.all()

    context = {
        'book': book,
    }
    return render(request, 'index.html', context)




def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username,email=email, password=password)
        return redirect('search/')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Using the renamed login function
            return render(request,'signup.html')  # Redirect to home page after login
        else:
            # Return an invalid login message
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def search(request):
    book = Product.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')

        results = Product.objects.filter(Q(title__icontains=search))
        context = {
            'result': results
        }
        return render(request, 'search.html', context)

    context = {
        'book': book,

    }

    return render(request, 'search.html', context)

