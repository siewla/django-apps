
from accounts.models import User, Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.


def view_register(request):
    # pass
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        city = request.POST['city']
        country = request.POST['country']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            return render(request, "accounts/register.html")

        try:
            user = User.objects.create_user(
                username, email, password, first_name=first_name, last_name=last_name)
            user.save()

            profile = Profile(city=city, country=country, user=user)
            profile.save()

        except IntegrityError:
            messages.error(request, "Username is taken already")
            return render(request, 'accounts/register.html')

        login(request, user)
        return redirect("bookstore:index")

    return render(request, "accounts/register.html")


def view_login(request):
    # pass
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("bookstore:index")
    else:
        messages.error(request, "username or password is incorrect")
        return render(request, "accounts/login.html")


def view_logout(request):
    logout(request)
    return redirect('accounts:login')
