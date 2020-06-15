# Generated by Django 3.0.7 on 2020-06-13 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64, verbose_name='Item')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('size', models.CharField(choices=[('small', 'small'), ('large', 'large')], default='small', max_length=5, verbose_name='Size')),
                ('category', models.CharField(choices=[('sicilian', 'Sicilian Pizza'), ('pizza', 'Neapolitan Pizza'), ('subs', 'Subs'), ('pasta', 'Pasta'), ('salads', 'Salads'), ('platters', 'Platters')], default='sicilian', max_length=10, verbose_name='Category')),
            ],
        ),
    ]
