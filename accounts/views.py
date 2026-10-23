
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .forms import RegisterForm, StyledLoginForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = StyledLoginForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("profile")
    else:
        form = StyledLoginForm(request)

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("profile")


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")
