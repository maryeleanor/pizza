from django.db import models


# Create your models here.
class Menu(models.Model):
    SIZE_CHOICES = (
        ('small', 'small'),
        ('large', 'large'),
    )
    CATEGORY_CHOICES = (
        ('sicilian', 'Sicilian Pizza'),
        ('pizza', 'Neapolitan Pizza'),
        ('subs', 'Subs'),
        ('pasta', 'Pasta'),
        ('salads', 'Salads'),
        ('platters', 'Platters'),
    )

    item = models.CharField("Item", max_length=64)
    price = models.DecimalField("Price", max_digits=5, decimal_places=2)
    size = models.CharField("Size", max_length=5, choices=SIZE_CHOICES, default='small')
    category = models.CharField("Category", max_length=10, choices=CATEGORY_CHOICES, default='sicilian')


    def __str__(self):
        return f"{self.category} - {self.size} {self.item} ({self.price})"


class PizzaToppings(models.Model):
    item = models.CharField("Topping", max_length=64)

    def __str__(self):
        return f"{self.item}"


class SandwichToppings(models.Model):
    item = models.CharField("Topping", max_length=64)
    price = models.DecimalField("Price", max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.item} ({self.price})"

# class Orders(models.Model):
#     customer_id = 


