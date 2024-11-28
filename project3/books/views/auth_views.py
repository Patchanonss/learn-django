# your_app/views/auth_views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from ..forms import UserRegisterForm, AuthenForm
from django.views import View

class Register(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(form.cleaned_data)
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login page after successful registration
        return render(request, 'register.html', {'form': form})

class LoginUser(View):
    def get(self, request):
        form = AuthenForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('get_all_books')  # Redirect to get_all_books page after successful login
            else:
                form.add_error(None, 'Invalid username or password')
                print("Authentication failed: Invalid username or password")
        else:
            print("Form is not valid")
            print(form.get_invalid_login_error())  # Print form errors to the console for debugging
        return render(request, 'login.html', {'form': form})

