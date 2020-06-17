from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("menu/", views.menu_page, name="menu"),
    path("about/", views.about, name="about"),
    path("order/", views.order, name="order"),
    path("register/", views.register, name="register"),
]
