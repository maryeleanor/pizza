from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "orders/index.html")


def menu(request):
    menu = "Here's the  menu from  the db"
    return render(request, "orders/menu.html",  {
        "menu": menu
    })