# Generated by Django 5.0.4 on 2024-04-03 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='closing_time',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='opening_time',
        ),
    ]