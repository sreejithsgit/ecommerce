# Generated by Django 4.2.4 on 2023-08-23 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0010_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]