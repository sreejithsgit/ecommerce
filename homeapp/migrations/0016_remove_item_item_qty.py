# Generated by Django 4.2.4 on 2023-09-06 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0015_item_item_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_qty',
        ),
    ]
