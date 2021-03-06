# Generated by Django 3.0.7 on 2020-06-16 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64, verbose_name='Item')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('size', models.CharField(choices=[('small', 'small'), ('large', 'large')], default='small', max_length=5, verbose_name='Size')),
                ('number_toppings_allowed', models.PositiveSmallIntegerField(default=0, verbose_name='Number of Toppings')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.category')),
            ],
        ),
        migrations.CreateModel(
            name='toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64, verbose_name='Topping')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_ordered', models.DateField(auto_now=True, verbose_name='Ordered at')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Subtotal')),
                ('total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveSmallIntegerField(verbose_name='Quantity')),
                ('notes', models.TextField(verbose_name='Notes')),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.menu')),
                ('orders', models.ManyToManyField(related_name='items', to='orders.orders')),
                ('toppings', models.ManyToManyField(blank=True, related_name='toppings_added', to='orders.toppings')),
            ],
        ),
    ]
