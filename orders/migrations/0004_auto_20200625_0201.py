# Generated by Django 3.0.7 on 2020-06-25 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_ordered', models.DateField(auto_now=True, verbose_name='Ordered at')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Subtotal')),
                ('total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total')),
                ('status', models.CharField(choices=[('Pen', 'Pending'), ('Rec', 'Received'), ('Del', 'Out for Delivery'), ('Com', 'Completed')], max_length=3)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveSmallIntegerField(default=1, verbose_name='Quantity')),
                ('notes', models.TextField(verbose_name='Notes')),
            ],
        ),
        migrations.RemoveField(
            model_name='order_placed',
            name='customer_id',
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Category'),
        ),
        migrations.RenameModel(
            old_name='included_topping',
            new_name='IncludedTopping',
        ),
        migrations.DeleteModel(
            name='item_in_order',
        ),
        migrations.DeleteModel(
            name='order_placed',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='included_toppings',
            field=models.ManyToManyField(blank=True, related_name='toppings_included', to='orders.IncludedTopping'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='menu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Menu'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='toppings_added', to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='orders.CartItem'),
        ),
    ]
