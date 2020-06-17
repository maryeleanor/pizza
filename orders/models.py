from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class category(models.Model):
    category_name = models.CharField("Category", max_length=64)

    def __str__(self):
        return f"{self.category_name}"

class menu(models.Model):
    SIZE_CHOICES = (
        ('small', 'small'),
        ('large', 'large'),
    )
    item = models.CharField("Item", max_length=64)
    price = models.DecimalField("Price", max_digits=5, decimal_places=2)
    size = models.CharField("Size", max_length=5, choices=SIZE_CHOICES, default='small')
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    number_toppings_allowed = models.PositiveSmallIntegerField("Number of Toppings", default=0)
    active = models.BooleanField("Active", default=True)

    def __str__(self):
        return f"{self.size} {self.item} ({self.price})"

class topping(models.Model):
    item = models.CharField("Topping", max_length=64)
    price = models.DecimalField("Price", max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.item} ({self.price})"

class included_topping(models.Model):
    item = models.CharField("Topping", max_length=64)

    def __str__(self):
        return f"{self.item}"

class order_placed(models.Model):
    customer_id = models.ForeignKey((User), on_delete=models.CASCADE)
    time_ordered = models.DateField("Ordered at", auto_now=True)
    subtotal = models.DecimalField("Subtotal", max_digits=5, decimal_places=2)
    total = models.DecimalField("Total", max_digits=5, decimal_places=2)

class item_in_order(models.Model):
    orders = models.ManyToManyField(order_placed, related_name="items")
    menu_id = models.ForeignKey((menu), on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField("Quantity")
    toppings = models.ManyToManyField(topping, blank=True, related_name="toppings_added")
    included_toppings = models.ManyToManyField(included_topping, blank=True, related_name="toppings_included")
    notes = models.TextField("Notes")


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField("First Name", max_length=64, blank=True)
    last_name = models.CharField("Last Name", max_length=64, blank=True)
    phone = models.CharField("Phone Number", max_length=12)
    