from django.contrib import admin
from .models import menu, category, topping,  included_topping, order_placed, item_in_order

# Register your models here.
admin.site.register(menu)
admin.site.register(category)
admin.site.register(topping)
admin.site.register(included_topping)
admin.site.register(order_placed)
admin.site.register(item_in_order)
