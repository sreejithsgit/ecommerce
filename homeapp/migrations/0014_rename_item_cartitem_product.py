# Generated by Django 4.2.4 on 2023-09-06 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0013_alter_image_item_image_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='item',
            new_name='product',
        ),
    ]