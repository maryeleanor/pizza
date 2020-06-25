from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


# Create your views here.
def index(request):
    return render(request, "orders/index.html")


def menu_page(request):
    # if request.method == 'POST':

    context = {
        "category": Category.objects.all(),
        "menu": Menu.objects.all(),
        "order_placed": Cart.objects.all()
    }
    return render(request, "orders/menu.html", context)


def about(request):
    about = "About Pinocchio's"
    return render(request, "orders/about.html",  {
        "about": about
    })


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'orders/register.html', {'form': form})

