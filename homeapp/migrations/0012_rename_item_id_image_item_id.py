# Generated by Django 4.2.4 on 2023-08-31 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0011_rename_images_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='Item_id',
            new_name='item_id',
        ),
    ]