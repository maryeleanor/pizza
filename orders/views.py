from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu

# Create your views here.
def index(request):
    return render(request, "orders/index.html")


def menu(request):
    context = {
        "menu": Menu.objects.all()
    }
    return render(request, "orders/menu.html", context)


def about(request):
    about = "About Pinocchio's"
    return render(request, "orders/about.html",  {
        "about": about
    })


def order(request):
    order = "Order Pinocchio's"
    return render(request, "orders/order.html",  {
        "order": order
    })