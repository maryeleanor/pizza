from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import menu, category, topping, included_topping, order_placed, item_in_order
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


# Create your views here.
def index(request):
    return render(request, "orders/index.html")


def menu_page(request):
    context = {
        "category": category.objects.all(),
        "menu": menu.objects.all(),
        "order_placed": order_placed.objects.all()
    }
    return render(request, "orders/menu.html", context)


def about(request):
    about = "About Pinocchio's"
    return render(request, "orders/about.html",  {
        "about": about
    })


@login_required
def order(request):
    order = "Order Pinocchio's"
    return render(request, "orders/order.html",  {
        "order": order
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

